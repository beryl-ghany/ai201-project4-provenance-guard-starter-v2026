"""
One structured record per /submit and /appeal, including refusals.

A line is one JSON object with named fields: timestamp, route, input,
output, duration_ms. print() is not this log. A refusal that never reaches
the file looks the same as a request that never arrived.
"""

import json
import threading
from datetime import datetime, timezone

import config

_lock = threading.Lock()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


def log_run(route: str, recorded_input: dict, output: dict, duration_ms: float) -> dict:
    """Append one run. duration_ms is handler time, not process start."""
    entry = {
        "timestamp": _now(),
        "route": route,
        "input": recorded_input,
        "output": output,
        "duration_ms": duration_ms,
    }
    config.LOG_DIR.mkdir(parents=True, exist_ok=True)
    line = json.dumps(entry, ensure_ascii=False)
    with _lock:
        with config.RUN_LOG.open("a", encoding="utf-8") as handle:
            handle.write(line + "\n")
    return entry


def read_entries(limit: int | None = None) -> list[dict]:
    """Oldest first. A bad line is skipped so one corrupt row does not hide the rest."""
    if not config.RUN_LOG.exists():
        return []
    entries = []
    for line in config.RUN_LOG.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return entries[-limit:] if limit else entries
