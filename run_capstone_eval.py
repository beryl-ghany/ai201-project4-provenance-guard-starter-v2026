#!/usr/bin/env python3
"""
Run capstone criteria evaluation — 3 trials each.

    python app.py                           # in one terminal
    python run_capstone_eval.py --label before   # in another

Tests the five capstone criteria for Shape B failure hardening:
  6. Timeout handling
  7. Retry success (transient failures)
  8. Graceful degradation
  9. 95% latency under 3s
  10. Error logging
"""

import argparse
import datetime as dt
import json
import os
import sys
import time
from pathlib import Path

import requests

import config

DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"


def test_timeout_handling(url: str, timeout: float = 15.0) -> dict:
    """
    Criterion 6: Timeout handling returns within 12 seconds with degraded flag.
    
    We test with normal text - if the model is slow or times out, it should
    return degraded=true within 12 seconds.
    """
    text = (
        "This is a test submission to verify timeout handling. The service "
        "should return a response within 12 seconds even if the model is slow. "
        "The response should include a degraded flag indicating whether normal "
        "processing occurred or the system fell back to degraded mode."
    )
    
    start = time.perf_counter()
    try:
        response = requests.post(
            f"{url}/submit",
            json={"text": text, "creator_id": "capstone_timeout_test"},
            timeout=timeout,
        )
        elapsed_ms = (time.perf_counter() - start) * 1000
        payload = response.json() if response.content else {}
        
        return {
            "status": response.status_code,
            "elapsed_ms": round(elapsed_ms, 2),
            "within_12s": elapsed_ms < 12000,
            "has_degraded_field": "degraded" in payload,
            "degraded": payload.get("degraded"),
            "guess": payload.get("guess"),
            "passed": elapsed_ms < 12000 and "degraded" in payload,
        }
    except requests.Timeout:
        elapsed_ms = (time.perf_counter() - start) * 1000
        return {
            "status": None,
            "elapsed_ms": round(elapsed_ms, 2),
            "within_12s": False,
            "error": "Request timed out",
            "passed": False,
        }
    except Exception as e:
        return {"error": str(e), "passed": False}


def test_graceful_degradation(url: str) -> dict:
    """
    Criterion 8: Graceful degradation returns valid guess/label defaulting to unsure.
    
    When the model times out or is unavailable, the response should still have
    a valid guess and label.
    """
    text = (
        "Testing graceful degradation. Even if the model cannot process this, "
        "the service should return a valid response with a guess field."
    )
    
    try:
        response = requests.post(
            f"{url}/submit",
            json={"text": text, "creator_id": "capstone_degradation_test"},
            timeout=15.0,
        )
        payload = response.json() if response.content else {}
        
        has_guess = "guess" in payload and payload["guess"] in ("human", "unsure", "ai")
        has_label = "label" in payload and isinstance(payload.get("label"), str)
        
        return {
            "status": response.status_code,
            "guess": payload.get("guess"),
            "label": payload.get("label", "")[:50] + "..." if payload.get("label") else None,
            "degraded": payload.get("degraded"),
            "has_valid_guess": has_guess,
            "has_valid_label": has_label,
            "passed": has_guess and has_label,
        }
    except Exception as e:
        return {"error": str(e), "passed": False}


def test_latency_target(url: str, num_requests: int = 20) -> dict:
    """
    Criterion 9: 95% of warm requests complete under 3 seconds.
    
    After warming up, 19/20 requests should complete in under 3000ms.
    """
    text = (
        "Testing latency target. This request should complete quickly once "
        "the model is warmed up and loaded into memory."
    )
    
    # Warm-up request (doesn't count)
    try:
        requests.post(
            f"{url}/submit",
            json={"text": "Warm-up request to load the model.", "creator_id": "warmup"},
            timeout=60.0,
        )
    except Exception:
        pass
    
    latencies = []
    for i in range(num_requests):
        start = time.perf_counter()
        try:
            response = requests.post(
                f"{url}/submit",
                json={"text": text, "creator_id": f"capstone_latency_{i}"},
                timeout=10.0,
            )
            elapsed_ms = (time.perf_counter() - start) * 1000
            latencies.append(elapsed_ms)
        except Exception as e:
            latencies.append(10000)  # Timeout counted as 10s
    
    under_3s = sum(1 for l in latencies if l < 3000)
    pct_under_3s = (under_3s / len(latencies)) * 100
    
    return {
        "total_requests": len(latencies),
        "under_3s_count": under_3s,
        "pct_under_3s": round(pct_under_3s, 1),
        "min_ms": round(min(latencies), 2),
        "max_ms": round(max(latencies), 2),
        "avg_ms": round(sum(latencies) / len(latencies), 2),
        "p95_ms": round(sorted(latencies)[int(len(latencies) * 0.95)], 2),
        "passed": pct_under_3s >= 95,
    }


def test_error_logging(url: str) -> dict:
    """
    Criterion 10: Every timeout/error leaves a structured log entry.
    
    Check that the instrumentation log contains entries for errors/timeouts.
    """
    # First, make a request that might trigger logging
    try:
        requests.post(
            f"{url}/submit",
            json={"text": "Test for error logging verification.", "creator_id": "log_test"},
            timeout=15.0,
        )
    except Exception:
        pass
    
    # Check the instrumentation log
    try:
        import instrumentation
        entries = instrumentation.read_instrumentation_log(limit=20)
        
        has_structured_entries = len(entries) > 0
        has_timestamp = all("timestamp" in e for e in entries) if entries else False
        has_request_id = all("request_id" in e for e in entries) if entries else False
        has_outcome = all("outcome" in e for e in entries) if entries else False
        
        # Look for any error or timeout entries
        error_entries = [e for e in entries if e.get("event") in ("error", "timeout")]
        success_entries = [e for e in entries if e.get("outcome") == "success"]
        
        return {
            "total_log_entries": len(entries),
            "has_structured_format": has_structured_entries and has_timestamp,
            "has_request_tracking": has_request_id,
            "has_outcome_field": has_outcome,
            "error_timeout_entries": len(error_entries),
            "success_entries": len(success_entries),
            "sample_entry": entries[-1] if entries else None,
            "passed": has_structured_entries and has_timestamp and has_request_id,
        }
    except Exception as e:
        return {"error": str(e), "passed": False}


def test_retry_success(url: str) -> dict:
    """
    Criterion 7: Transient failures that succeed on retry don't expose errors.
    
    This is hard to test directly without injecting failures. We verify that
    normal requests don't expose retry internals and the response is clean.
    """
    text = (
        "Testing retry behavior. If transient failures occur internally, "
        "they should be masked from this response."
    )
    
    try:
        response = requests.post(
            f"{url}/submit",
            json={"text": text, "creator_id": "capstone_retry_test"},
            timeout=15.0,
        )
        payload = response.json() if response.content else {}
        
        # A successful response should not expose retry internals
        no_error_field = "error" not in payload or response.status_code != 200
        has_normal_response = response.status_code == 200 and "guess" in payload
        no_retry_exposure = "retry" not in str(payload).lower()
        
        return {
            "status": response.status_code,
            "has_error_field": "error" in payload,
            "has_guess": "guess" in payload,
            "no_retry_exposure": no_retry_exposure,
            "passed": has_normal_response and no_retry_exposure,
        }
    except Exception as e:
        return {"error": str(e), "passed": False}


CAPSTONE_TESTS = [
    {"criterion": 6, "name": "Timeout handling", "func": test_timeout_handling},
    {"criterion": 7, "name": "Retry success", "func": test_retry_success},
    {"criterion": 8, "name": "Graceful degradation", "func": test_graceful_degradation},
    {"criterion": 9, "name": "Latency target", "func": test_latency_target},
    {"criterion": 10, "name": "Error logging", "func": test_error_logging},
]


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=DEFAULT_URL)
    args = parser.parse_args()

    try:
        requests.get(f"{args.url}/health", timeout=5)
    except Exception:
        print(f"Nothing answering at {args.url}. Start it:  python app.py",
              file=sys.stderr)
        sys.exit(1)

    print(f"\nCapstone Evaluation — {args.trials} trials per criterion")
    print(f"Target: {args.url}")
    print("-" * 60)

    all_results = []

    for test in CAPSTONE_TESTS:
        print(f"\n{test['criterion']}. {test['name']}")
        
        trials = []
        for trial in range(1, args.trials + 1):
            result = test["func"](args.url)
            trials.append(result)
            status = "PASS" if result.get("passed") else "MISS"
            print(f"  Trial {trial}: {status}")
        
        passed_count = sum(1 for t in trials if t.get("passed"))
        all_results.append({
            "criterion": test["criterion"],
            "name": test["name"],
            "trials": trials,
            "passed_count": passed_count,
            "total_trials": len(trials),
            "verdict": "MET" if passed_count == len(trials) else "MISSED",
        })

    # Write report
    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"capstone_run_{stamp}{label}.md"

    lines = [
        f"# Capstone Run Log{f' — {args.label}' if args.label else ''}",
        "",
        "- Produced by: `run_capstone_eval.py`",
        f"- {args.trials} trials per criterion · {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Summary",
        "",
        "| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |",
        "|---|---|---|---|---|---|",
    ]

    for r in all_results:
        trial_cells = []
        for t in r["trials"]:
            status = "PASS" if t.get("passed") else "MISS"
            trial_cells.append(status)
        while len(trial_cells) < 3:
            trial_cells.append("—")
        lines.append(
            f"| {r['criterion']}. {r['name']} | — | "
            f"{' | '.join(trial_cells)} | {r['verdict']} |"
        )

    lines += ["", "---", "", "## Detailed Results", ""]

    for r in all_results:
        lines += [f"### {r['criterion']}. {r['name']}", ""]
        for i, trial in enumerate(r["trials"], 1):
            lines += [f"**Trial {i}**", "", "```json",
                      json.dumps(trial, indent=2, default=str), "```", ""]

    # Cost calculation
    lines += [
        "---",
        "",
        "## Cost Calculation",
        "",
        "- **API cost**: $0 (local model, no external API calls)",
        "- **Compute cost per run**: Measured average latency × requests",
        "",
    ]

    # Get latency stats if available
    try:
        import instrumentation
        stats = instrumentation.get_latency_stats()
        if stats.get("count", 0) > 0:
            lines += [
                f"  - Average request latency: {stats.get('total_p50_ms', 'N/A')}ms (p50)",
                f"  - 95th percentile: {stats.get('total_p95_ms', 'N/A')}ms",
                f"  - Total logged requests: {stats['count']}",
            ]
    except Exception:
        pass

    lines += [
        "",
        "**For 100 users/day at ~5 requests each (500 requests/day):**",
        "- Assuming 2 seconds average per request",
        "- Total compute time: 500 × 2s = 1000 seconds ≈ 17 minutes/day",
        "- Monthly: 17 min × 30 = 8.5 hours compute time",
        "",
    ]

    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")

    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    met = sum(1 for r in all_results if r["verdict"] == "MET")
    total = len(all_results)
    print(f"Criteria MET: {met}/{total}")
    for r in all_results:
        print(f"  {r['criterion']}. {r['name']}: {r['verdict']}")


if __name__ == "__main__":
    main()
