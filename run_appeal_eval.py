#!/usr/bin/env python3
"""Criterion 4: submit five pieces, appeal each, check log — three trials."""

import argparse
import datetime as dt
import json
import sys

import config

DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"

TEXTS = [
    "Appeal test one: I wrote this on the train, half distracted, all mine.",
    "Appeal test two: my sister proofread typos only; the ideas are still mine.",
    "Appeal test three: short note to myself about groceries and overdue emails.",
    "Appeal test four: rant about parking tickets. Petty, human, unfortunately accurate.",
    "Appeal test five: draft email I never sent to my professor about extensions.",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="before")
    parser.add_argument("--url", default=DEFAULT_URL)
    args = parser.parse_args()

    try:
        import requests
    except ImportError:
        print("pip install -r requirements.txt", file=sys.stderr)
        sys.exit(1)

    trials = []
    for trial in range(1, args.trials + 1):
        trial_rows = []
        for i, text in enumerate(TEXTS, 1):
            sub = requests.post(
                f"{args.url}/submit",
                json={"text": text, "creator_id": f"appeal_eval_{trial}_{i}"},
                timeout=120,
            )
            sub_json = sub.json() if sub.content else {}
            cid = sub_json.get("content_id")
            ok_submit = sub.status_code == 200 and cid

            appeal_ok = False
            appeal_status = None
            if ok_submit:
                app = requests.post(
                    f"{args.url}/appeal",
                    json={"content_id": cid, "reasoning": "I wrote this myself."},
                    timeout=30,
                )
                appeal_status = app.status_code
                appeal_ok = app.status_code == 200 and (app.json() or {}).get("ok")

            log_ok = False
            if cid:
                log = requests.get(f"{args.url}/log", timeout=30)
                entries = (log.json() or {}).get("entries", [])
                for cid_entries in [e for e in entries if e.get("content_id") == cid]:
                    if cid_entries.get("event") == "appeal" and cid_entries.get("status") == "under_review":
                        log_ok = True

            trial_rows.append({
                "submit_status": sub.status_code,
                "content_id": cid,
                "appeal_status": appeal_status,
                "appeal_ok": appeal_ok,
                "log_under_review": log_ok,
            })
        success = sum(1 for r in trial_rows if r["appeal_ok"] and r["log_under_review"])
        trials.append({"trial": trial, "success": success, "rows": trial_rows})
        print(f"trial {trial}: {success}/5 appeals ok with under_review log line")

    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    path = config.RESULTS_DIR / f"appeal_run_{stamp}_{args.label}.json"
    path.write_text(json.dumps({"trials": trials}, indent=2), encoding="utf-8")
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
