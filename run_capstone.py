#!/usr/bin/env python3
"""
Three trials of the five capstone criteria, against a server that is already up.

    python run_capstone.py --label before

Writes results/capstone_<label>.json and prints the run-log table.
Does not change the service between trials.
"""

import argparse
import json
import time
from pathlib import Path

import requests

import capstone_cases
import config

ROOT = Path(__file__).parent


def _body(response):
    try:
        return response.json()
    except ValueError:
        return {"raw": response.text[:300]}


def post_submit(base: str, text: str, creator: str, timeout: float):
    started = time.perf_counter()
    response = requests.post(
        f"{base}/submit",
        json={"text": text, "creator_id": creator},
        timeout=timeout,
    )
    elapsed_ms = round((time.perf_counter() - started) * 1000, 1)
    return response.status_code, _body(response), elapsed_ms


def file_size(path: Path) -> int:
    return path.stat().st_size if path.exists() else 0


def new_records(path: Path, offset: int) -> list[dict]:
    if not path.exists():
        return []
    data = path.read_bytes()[offset:]
    records = []
    for line in data.decode("utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        records.append(json.loads(line))
    return records


def _has_guess(record: dict) -> bool:
    return "guess" in record and record.get("guess") is not None


def criterion_1(base, trial, timeout):
    """5 of 5 non-writing bodies return 400 not_writing and no guess."""
    rows = []
    hits = 0
    for index, text in enumerate(capstone_cases.NOT_WRITING, start=1):
        status, body, elapsed = post_submit(
            base, text, f"cap-nw-t{trial}-n{index}", timeout
        )
        ok = status == 400 and body.get("error") == "not_writing" and "guess" not in body
        hits += int(ok)
        rows.append({
            "text": text,
            "status": status,
            "body": body,
            "elapsed_ms": elapsed,
            "ok": ok,
        })
    return hits, len(capstone_cases.NOT_WRITING), rows


def criterion_2(base, trial, timeout):
    """Each of those five adds no audit row that carries a guess."""
    rows = []
    hits = 0
    for index, text in enumerate(capstone_cases.NOT_WRITING, start=1):
        offset = file_size(config.AUDIT_LOG)
        status, body, elapsed = post_submit(
            base, text, f"cap-audit-t{trial}-n{index}", timeout
        )
        added = new_records(config.AUDIT_LOG, offset)
        guess_rows = [row for row in added if _has_guess(row)]
        ok = status == 400 and body.get("error") == "not_writing" and not guess_rows
        hits += int(ok)
        rows.append({
            "status": status,
            "error": body.get("error"),
            "elapsed_ms": elapsed,
            "audit_added": added,
            "guess_rows": len(guess_rows),
            "ok": ok,
        })
    return hits, len(capstone_cases.NOT_WRITING), rows


def criterion_3(base, trial, timeout):
    """Each refusal is one run record: timestamp, input, output 400, duration under 200 ms."""
    rows = []
    hits = 0
    for index, text in enumerate(capstone_cases.NOT_WRITING, start=1):
        offset = file_size(config.RUN_LOG)
        status, body, elapsed = post_submit(
            base, text, f"cap-log-t{trial}-n{index}", timeout
        )
        added = new_records(config.RUN_LOG, offset)
        record = added[-1] if added else None
        ok = False
        if (
            status == 400
            and body.get("error") == "not_writing"
            and record is not None
            and len(added) == 1
        ):
            output = record.get("output") or {}
            duration = record.get("duration_ms")
            ok = (
                isinstance(record.get("timestamp"), str)
                and isinstance(record.get("input"), dict)
                and output.get("status") == 400
                and output.get("error") == "not_writing"
                and isinstance(duration, (int, float))
                and duration < 200
            )
        hits += int(ok)
        rows.append({
            "status": status,
            "elapsed_ms": elapsed,
            "record": record,
            "added": len(added),
            "ok": ok,
        })
    return hits, len(capstone_cases.NOT_WRITING), rows


def criterion_4(base, trial, timeout):
    """Five ordinary paragraphs still return 200 with guess and both scores."""
    rows = []
    hits = 0
    for index, text in enumerate(capstone_cases.WRITING, start=1):
        status, body, elapsed = post_submit(
            base, text, f"cap-prose-t{trial}-n{index}", timeout
        )
        ok = (
            status == 200
            and isinstance(body.get("guess"), str)
            and isinstance(body.get("model_score"), (int, float))
            and isinstance(body.get("style_score"), (int, float))
        )
        hits += int(ok)
        rows.append({
            "text": text,
            "status": status,
            "body": body,
            "elapsed_ms": elapsed,
            "ok": ok,
        })
    return hits, len(capstone_cases.WRITING), rows


def criterion_5(base, trial, timeout):
    """After the model is loaded, 9 of 10 sequential warm submits finish within 3 s."""
    health = requests.get(f"{base}/health", timeout=30).json()
    if not health.get("detector_loaded"):
        post_submit(base, capstone_cases.LATENCY_TEXT, f"cap-warm-t{trial}", timeout)
        health = requests.get(f"{base}/health", timeout=30).json()
    loaded = bool(health.get("detector_loaded"))
    rows = []
    hits = 0
    for index in range(1, 11):
        status, body, elapsed = post_submit(
            base,
            capstone_cases.LATENCY_TEXT,
            f"cap-lat-t{trial}-n{index}",
            timeout,
        )
        ok = loaded and status == 200 and elapsed <= 3000
        hits += int(ok)
        rows.append({
            "status": status,
            "elapsed_ms": elapsed,
            "guess": body.get("guess"),
            "ok": ok,
        })
    return hits, 10, {"detector_loaded": loaded, "calls": rows}


def repeated_letter_probe(base, trial, timeout):
    status, body, elapsed = post_submit(
        base, capstone_cases.REPEATED_LETTER, f"cap-repeat-t{trial}", timeout
    )
    return {
        "status": status,
        "guess": body.get("guess"),
        "error": body.get("error"),
        "combined_score": body.get("combined_score"),
        "elapsed_ms": elapsed,
    }


def measure_cost(base, timeout):
    """Ten warm submits. Average client time is the per-run cost."""
    samples = []
    for index in range(1, 11):
        status, body, elapsed = post_submit(
            base, capstone_cases.LATENCY_TEXT, f"cap-cost-n{index}", timeout
        )
        samples.append({
            "status": status,
            "elapsed_ms": elapsed,
            "guess": body.get("guess"),
        })
    times = [row["elapsed_ms"] for row in samples if row["status"] == 200]
    average = round(sum(times) / len(times), 1) if times else None
    return {"samples": samples, "average_ms": average, "n": len(times)}


CHECKS = [
    ("1. Non-writing returns 400 not_writing", "5 of 5", criterion_1),
    ("2. Non-writing adds no guess row", "5 of 5", criterion_2),
    ("3. Refusal is logged under 200 ms", "5 of 5", criterion_3),
    ("4. Ordinary paragraphs still score", "5 of 5", criterion_4),
    ("5. Warm submit within 3 seconds", "9 of 10", criterion_5),
]


def run_trials(base, timeout):
    trials = []
    for trial in (1, 2, 3):
        one = {"trial": trial, "criteria": [], "probe_repeated_letter": None}
        for name, target, fn in CHECKS:
            hits, total, detail = fn(base, trial, timeout)
            one["criteria"].append({
                "name": name,
                "target": target,
                "hits": hits,
                "total": total,
                "score": f"{hits}/{total}",
                "detail": detail,
            })
        one["probe_repeated_letter"] = repeated_letter_probe(base, trial, timeout)
        trials.append(one)
        print(f"trial {trial} done", flush=True)
    return trials


def table(trials):
    lines = [
        "| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |",
        "|---|---|---|---|---|---|",
    ]
    for index, (name, target, _) in enumerate(CHECKS):
        scores = [trials[n]["criteria"][index]["score"] for n in range(3)]
        needed = int(target.split()[0])
        met = all(int(score.split("/")[0]) >= needed for score in scores)
        verdict = "MET" if met else "MISSED"
        lines.append(
            f"| {name} | {target} | {scores[0]} | {scores[1]} | {scores[2]} | {verdict} |"
        )
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", required=True, choices=("before", "after"))
    parser.add_argument("--base", default="http://127.0.0.1:5000")
    parser.add_argument("--timeout", type=float, default=180)
    parser.add_argument("--skip-cost", action="store_true")
    args = parser.parse_args()

    health = requests.get(f"{args.base}/health", timeout=30)
    health.raise_for_status()

    trials = run_trials(args.base, args.timeout)
    cost = None if args.skip_cost else measure_cost(args.base, args.timeout)
    payload = {
        "label": args.label,
        "base": args.base,
        "table": table(trials),
        "trials": trials,
        "cost": cost,
    }
    config.RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out = config.RESULTS_DIR / f"capstone_{args.label}.json"
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(payload["table"])
    if cost:
        print(f"cost_average_ms {cost['average_ms']} over {cost['n']} runs")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
