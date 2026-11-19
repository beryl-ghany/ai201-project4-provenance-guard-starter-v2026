"""
Instrumentation for Provenance Guard — timing and structured logging.

Tracks latency for each stage of request processing and records structured
JSON log entries for monitoring and debugging.
"""

import json
import threading
import time
import uuid
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

import config


@dataclass
class RequestTiming:
    """Tracks timing for a single request across all stages."""
    request_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    start_time: float = field(default_factory=time.perf_counter)
    stages: dict[str, float] = field(default_factory=dict)
    input_length: int = 0
    outcome: str = "success"
    degraded_mode: bool = False
    error_stage: str | None = None
    error_message: str | None = None

    def record_stage(self, name: str, duration_ms: float) -> None:
        self.stages[name] = duration_ms

    def total_latency_ms(self) -> float:
        return (time.perf_counter() - self.start_time) * 1000

    def to_dict(self) -> dict[str, Any]:
        return {
            "timestamp": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
            "request_id": self.request_id,
            "input_length": self.input_length,
            "model_latency_ms": self.stages.get("model_signal"),
            "style_latency_ms": self.stages.get("style_signal"),
            "combine_latency_ms": self.stages.get("combine"),
            "total_latency_ms": round(self.total_latency_ms(), 2),
            "outcome": self.outcome,
            "degraded_mode": self.degraded_mode,
            "error_stage": self.error_stage,
            "error_message": self.error_message,
            "stages": self.stages,
        }


_current_timing = threading.local()


def get_current_timing() -> RequestTiming | None:
    return getattr(_current_timing, "timing", None)


def set_current_timing(timing: RequestTiming | None) -> None:
    _current_timing.timing = timing


@contextmanager
def request_context(input_length: int = 0):
    """Context manager for tracking request timing."""
    timing = RequestTiming(input_length=input_length)
    set_current_timing(timing)
    try:
        yield timing
    finally:
        set_current_timing(None)


@contextmanager
def timed_stage(name: str):
    """Context manager for timing a specific stage."""
    start = time.perf_counter()
    try:
        yield
    finally:
        duration_ms = (time.perf_counter() - start) * 1000
        timing = get_current_timing()
        if timing:
            timing.record_stage(name, round(duration_ms, 2))


_log_lock = threading.Lock()
INSTRUMENTATION_LOG = config.LOG_DIR / "instrumentation.jsonl"


def log_request(timing: RequestTiming) -> None:
    """Write timing data to the instrumentation log."""
    config.LOG_DIR.mkdir(parents=True, exist_ok=True)
    entry = timing.to_dict()
    line = json.dumps(entry, ensure_ascii=False)
    with _log_lock:
        with INSTRUMENTATION_LOG.open("a", encoding="utf-8") as f:
            f.write(line + "\n")


def log_error(
    timing: RequestTiming | None,
    stage: str,
    error_type: str,
    message: str,
    duration_ms: float | None = None,
) -> None:
    """Log an error event with structured data."""
    config.LOG_DIR.mkdir(parents=True, exist_ok=True)
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
        "event": error_type,
        "outcome": error_type,
        "stage": stage,
        "message": message,
        "request_id": timing.request_id if timing else None,
        "duration_ms": duration_ms,
    }
    line = json.dumps(entry, ensure_ascii=False)
    with _log_lock:
        with INSTRUMENTATION_LOG.open("a", encoding="utf-8") as f:
            f.write(line + "\n")


def log_timeout(timing: RequestTiming | None, stage: str, duration_ms: float) -> None:
    """Log a timeout event."""
    log_error(timing, stage, "timeout", f"Timeout after {duration_ms:.0f}ms", duration_ms)


def read_instrumentation_log(limit: int | None = None) -> list[dict]:
    """Read the instrumentation log, oldest first."""
    if not INSTRUMENTATION_LOG.exists():
        return []

    entries = []
    for line in INSTRUMENTATION_LOG.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            continue

    return entries[-limit:] if limit else entries


def clear_instrumentation_log() -> int:
    """Clear the instrumentation log. Returns count of entries cleared."""
    count = len(read_instrumentation_log())
    if INSTRUMENTATION_LOG.exists():
        INSTRUMENTATION_LOG.unlink()
    return count


def get_latency_stats(entries: list[dict] | None = None) -> dict[str, Any]:
    """Calculate latency statistics from log entries."""
    if entries is None:
        entries = read_instrumentation_log()

    success_entries = [e for e in entries if e.get("outcome") == "success"]
    if not success_entries:
        return {"count": 0}

    total_latencies = [e["total_latency_ms"] for e in success_entries if e.get("total_latency_ms")]
    model_latencies = [e["model_latency_ms"] for e in success_entries if e.get("model_latency_ms")]
    style_latencies = [e["style_latency_ms"] for e in success_entries if e.get("style_latency_ms")]

    def percentile(data: list[float], p: float) -> float | None:
        if not data:
            return None
        sorted_data = sorted(data)
        idx = int(len(sorted_data) * p / 100)
        return sorted_data[min(idx, len(sorted_data) - 1)]

    return {
        "count": len(success_entries),
        "total_p50_ms": percentile(total_latencies, 50),
        "total_p95_ms": percentile(total_latencies, 95),
        "total_p99_ms": percentile(total_latencies, 99),
        "model_p50_ms": percentile(model_latencies, 50),
        "model_p95_ms": percentile(model_latencies, 95),
        "style_p50_ms": percentile(style_latencies, 50),
        "style_p95_ms": percentile(style_latencies, 95),
    }


def get_latency_breakdown(entries: list[dict] | None = None) -> dict[str, Any]:
    """
    Get detailed latency breakdown showing where time goes.
    Stretch goal B: Latency breakdown.
    """
    if entries is None:
        entries = read_instrumentation_log()

    success_entries = [e for e in entries if e.get("outcome") == "success" and e.get("stages")]
    if not success_entries:
        return {"count": 0, "breakdown": {}}

    # Aggregate stage times
    stage_times: dict[str, list[float]] = {}
    for entry in success_entries:
        for stage, duration in entry.get("stages", {}).items():
            if stage not in stage_times:
                stage_times[stage] = []
            stage_times[stage].append(duration)

    # Calculate averages and percentages
    total_avg = sum(sum(times) / len(times) for times in stage_times.values())
    
    breakdown = {}
    for stage, times in sorted(stage_times.items()):
        avg_ms = sum(times) / len(times)
        pct = (avg_ms / total_avg * 100) if total_avg > 0 else 0
        breakdown[stage] = {
            "avg_ms": round(avg_ms, 2),
            "min_ms": round(min(times), 2),
            "max_ms": round(max(times), 2),
            "pct_of_total": round(pct, 1),
            "sample_count": len(times),
        }

    return {
        "count": len(success_entries),
        "total_avg_ms": round(total_avg, 2),
        "breakdown": breakdown,
    }
