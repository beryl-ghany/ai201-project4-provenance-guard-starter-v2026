#!/usr/bin/env python3
"""
Load test for Provenance Guard — Stretch Goal C.

Sends requests at 10x normal rate and reports:
- Response time distribution
- Error rate
- Any degradation observed

    python app.py                    # in one terminal
    python run_load_test.py          # in another
"""

import argparse
import datetime as dt
import json
import statistics
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests

import config

DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"

SAMPLE_TEXTS = [
    "I stayed up until two finishing this draft. My sentences are all over the place.",
    "The implementation requires careful consideration of several key factors.",
    "Rain on the window during office hours. Three students canceled.",
    "The bus was late again so I walked. Cold air, wet sneakers.",
    "In conclusion, it is worth noting that the aforementioned considerations matter.",
]


def send_request(url: str, text: str, creator_id: str, timeout: float = 30.0) -> dict:
    """Send a single request and return timing/result info."""
    start = time.perf_counter()
    try:
        response = requests.post(
            f"{url}/submit",
            json={"text": text, "creator_id": creator_id},
            timeout=timeout,
        )
        elapsed_ms = (time.perf_counter() - start) * 1000
        payload = response.json() if response.content else {}
        
        return {
            "status": response.status_code,
            "elapsed_ms": round(elapsed_ms, 2),
            "degraded": payload.get("degraded", False),
            "guess": payload.get("guess"),
            "error": None,
        }
    except requests.Timeout:
        elapsed_ms = (time.perf_counter() - start) * 1000
        return {
            "status": None,
            "elapsed_ms": round(elapsed_ms, 2),
            "degraded": None,
            "guess": None,
            "error": "timeout",
        }
    except Exception as e:
        elapsed_ms = (time.perf_counter() - start) * 1000
        return {
            "status": None,
            "elapsed_ms": round(elapsed_ms, 2),
            "degraded": None,
            "guess": None,
            "error": str(type(e).__name__),
        }


def run_load_test(
    url: str,
    total_requests: int = 50,
    concurrency: int = 10,
    delay_between_batches: float = 0.1,
) -> dict:
    """
    Run load test with specified concurrency.
    
    Normal rate might be ~5 requests/minute.
    10x rate = 50 requests/minute = ~0.8 requests/second.
    """
    results = []
    start_time = time.perf_counter()
    
    print(f"Sending {total_requests} requests with concurrency {concurrency}...")
    
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = []
        for i in range(total_requests):
            text = SAMPLE_TEXTS[i % len(SAMPLE_TEXTS)]
            creator_id = f"load_test_{i}"
            future = executor.submit(send_request, url, text, creator_id)
            futures.append(future)
            
            # Small delay to avoid overwhelming too quickly
            if (i + 1) % concurrency == 0:
                time.sleep(delay_between_batches)
        
        for i, future in enumerate(as_completed(futures)):
            result = future.result()
            results.append(result)
            if (i + 1) % 10 == 0:
                print(f"  Completed {i + 1}/{total_requests}")
    
    total_time = time.perf_counter() - start_time
    
    # Calculate statistics
    latencies = [r["elapsed_ms"] for r in results if r["elapsed_ms"]]
    errors = [r for r in results if r.get("error") or r.get("status") != 200]
    degraded = [r for r in results if r.get("degraded") is True]
    rate_limited = [r for r in results if r.get("status") == 429]
    
    return {
        "total_requests": total_requests,
        "total_time_seconds": round(total_time, 2),
        "requests_per_second": round(total_requests / total_time, 2),
        "concurrency": concurrency,
        "latency": {
            "min_ms": round(min(latencies), 2) if latencies else None,
            "max_ms": round(max(latencies), 2) if latencies else None,
            "avg_ms": round(statistics.mean(latencies), 2) if latencies else None,
            "median_ms": round(statistics.median(latencies), 2) if latencies else None,
            "p95_ms": round(sorted(latencies)[int(len(latencies) * 0.95)], 2) if latencies else None,
            "p99_ms": round(sorted(latencies)[int(len(latencies) * 0.99)], 2) if latencies else None,
            "stdev_ms": round(statistics.stdev(latencies), 2) if len(latencies) > 1 else None,
        },
        "success_count": len([r for r in results if r.get("status") == 200]),
        "error_count": len(errors),
        "error_rate_pct": round(len(errors) / total_requests * 100, 2),
        "degraded_count": len(degraded),
        "degraded_rate_pct": round(len(degraded) / total_requests * 100, 2),
        "rate_limited_count": len(rate_limited),
        "results": results,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--requests", type=int, default=50, help="Total requests to send")
    parser.add_argument("--concurrency", type=int, default=10, help="Concurrent requests")
    args = parser.parse_args()

    try:
        health = requests.get(f"{args.url}/health", timeout=5).json()
        print(f"Service: {args.url}")
        print(f"Model: {health.get('detector_model')}")
        print(f"Model loaded: {health.get('detector_loaded')}")
        print()
    except Exception:
        print(f"Nothing answering at {args.url}. Start it:  python app.py",
              file=sys.stderr)
        sys.exit(1)

    # Warm up
    print("Warming up model...")
    send_request(args.url, "Warm up request to load the model.", "warmup", timeout=60)
    print()

    # Run load test
    result = run_load_test(
        url=args.url,
        total_requests=args.requests,
        concurrency=args.concurrency,
    )

    # Print summary
    print("\n" + "=" * 60)
    print("LOAD TEST RESULTS")
    print("=" * 60)
    print(f"Total requests: {result['total_requests']}")
    print(f"Total time: {result['total_time_seconds']}s")
    print(f"Throughput: {result['requests_per_second']} req/s")
    print()
    print("Response Time Distribution:")
    print(f"  Min:    {result['latency']['min_ms']}ms")
    print(f"  Median: {result['latency']['median_ms']}ms")
    print(f"  Avg:    {result['latency']['avg_ms']}ms")
    print(f"  P95:    {result['latency']['p95_ms']}ms")
    print(f"  P99:    {result['latency']['p99_ms']}ms")
    print(f"  Max:    {result['latency']['max_ms']}ms")
    print()
    print(f"Success rate: {result['success_count']}/{result['total_requests']} ({100 - result['error_rate_pct']}%)")
    print(f"Error rate: {result['error_rate_pct']}%")
    print(f"Degraded responses: {result['degraded_count']} ({result['degraded_rate_pct']}%)")
    print(f"Rate limited: {result['rate_limited_count']}")

    # Write report
    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    path = config.RESULTS_DIR / f"load_test_{stamp}.md"

    lines = [
        "# Load Test Results",
        "",
        f"- Produced by: `run_load_test.py`",
        f"- {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Configuration",
        "",
        f"- Total requests: {result['total_requests']}",
        f"- Concurrency: {result['concurrency']}",
        f"- Target URL: {args.url}",
        "",
        "## Summary",
        "",
        f"- Total time: {result['total_time_seconds']}s",
        f"- Throughput: {result['requests_per_second']} requests/second",
        "",
        "## Response Time Distribution",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Min | {result['latency']['min_ms']}ms |",
        f"| Median | {result['latency']['median_ms']}ms |",
        f"| Average | {result['latency']['avg_ms']}ms |",
        f"| P95 | {result['latency']['p95_ms']}ms |",
        f"| P99 | {result['latency']['p99_ms']}ms |",
        f"| Max | {result['latency']['max_ms']}ms |",
        f"| Std Dev | {result['latency']['stdev_ms']}ms |",
        "",
        "## Error Analysis",
        "",
        f"- Success count: {result['success_count']}",
        f"- Error count: {result['error_count']}",
        f"- Error rate: {result['error_rate_pct']}%",
        f"- Degraded responses: {result['degraded_count']} ({result['degraded_rate_pct']}%)",
        f"- Rate limited: {result['rate_limited_count']}",
        "",
        "## Raw Results",
        "",
        "```json",
        json.dumps({k: v for k, v in result.items() if k != "results"}, indent=2),
        "```",
        "",
    ]

    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
