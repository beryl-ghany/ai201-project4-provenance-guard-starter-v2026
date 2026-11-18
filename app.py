#!/usr/bin/env python3
"""
Provenance Guard — the web service.

    python app.py

Then, in another terminal:

    curl -X POST http://127.0.0.1:5000/ping \
      -H "Content-Type: application/json" \
      -d '{"message": "hello"}'

That's the example route. It works right now, before you've written anything.
**Leave it alone** — it's your control. When something breaks later, check that
`/ping` still answers: if it does, the problem is in your handler; if it
doesn't, it's the service itself.

Routes:

    POST /ping        the worked example. Already works. Don't edit it
    POST /submit      ← YOU BUILD THIS (Milestone 3, 4, 5)
    POST /appeal      ← YOU BUILD THIS (Milestone 5)
    GET  /log         the audit log. Already works
    GET  /health      is the service up, and is the model loaded
"""

import time
import uuid

from flask import Flask, g, jsonify, request

import audit
import config
import detector
import runlog
import scoring
import stylometry
import writing_check

app = Flask(__name__)


@app.before_request
def _mark_start():
    """Stamp the request before the rate limiter can reject it."""
    g.started = time.perf_counter()


# ── Rate limiting — UNIT 8 ────────────────────────────────────────────────────
# Off until you turn it on. In unit 8, Milestone 1:
#
#   1. Set RATE_LIMITING_ENABLED = True in config.py (or AI201_RATE_LIMITS=1)
#   2. Choose your numbers there
#   3. Uncomment the @limiter.limit(...) line on /submit below
#
# The order doesn't matter. While limiting is off, that decorator is a no-op
# that quietly does nothing, so uncommenting it early costs you nothing — but
# it also means no 429 until you've done step 1.
#
# The storage backend is preconfigured, which stops Flask-Limiter printing a
# warning on every start. In-memory is right for one laptop and wrong for
# anything real — a restart forgets every count.

class _LimiterOff:
    """
    Stands in for the real limiter while rate limiting is off.

    It makes @limiter.limit(...) a decorator that returns the route
    untouched, so uncommenting the line before you flip the setting is
    harmless instead of a crash on startup.
    """

    def limit(self, *args, **kwargs):
        return lambda view: view


limiter = _LimiterOff()
if config.RATE_LIMITING_ENABLED:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    def rate_limit_key():
        """
        Who a request counts against.

        Falling back to the caller's address is the easy version. Unit 8's
        stretch asks about per-creator limits instead — and the difference
        matters: one script can look like a thousand callers, and one household
        can look like one.
        """
        payload = request.get_json(silent=True)
        # A body that parses as JSON but isn't an object — a bare list or
        # string — has no .get. Without this guard the key function raises
        # BEFORE the route runs, and a malformed request becomes a 500 that
        # looks like your handler crashed when your handler never ran.
        if not isinstance(payload, dict):
            return get_remote_address()
        creator = payload.get("creator_id")
        return creator if isinstance(creator, str) and creator.strip() else get_remote_address()

    limiter = Limiter(
        key_func=rate_limit_key,
        app=app,
        storage_uri=config.RATE_LIMIT_STORAGE,
        default_limits=[],
    )

    @app.errorhandler(429)
    def rate_limited(exc):
        """
        A rejected request still leaves a trace.

        ⚠️ An attack that shows up only as an absence is one you'll never find.
        """
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            payload = {}
        creator = payload.get("creator_id", "unknown")
        if not isinstance(creator, str) or not creator.strip():
            creator = "unknown"
        audit.log_rejection(
            creator_id=creator,
            reason="rate_limited",
            limit=str(exc.description),
        )
        body = {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly.",
            "limit": str(exc.description),
        }
        started = getattr(g, "started", None)
        duration_ms = round((time.perf_counter() - started) * 1000, 1) if started else 0.0
        text = payload.get("text")
        runlog.log_run(
            "/submit",
            {
                "creator_id": creator,
                "text_excerpt": text[:200] if isinstance(text, str) else None,
                "text_chars": len(text) if isinstance(text, str) else None,
                "letter_ratio": None,
            },
            {"status": 429, "error": "rate_limited"},
            duration_ms,
        )
        return jsonify(body), 429


# ── The worked example. Already works. Don't edit. ────────────────────────────

@app.post("/ping")
def ping():
    """
    Everything a route needs, in six lines.

    JSON arrives as a dict. You pull things out of it. You return a dict and
    the framework turns it into a response. That's the whole idea.
    """
    payload = request.get_json(silent=True) or {}
    return jsonify({
        "ok": True,
        "you_sent": payload.get("message"),
        "service": "provenance-guard",
    })


@app.get("/health")
def health():
    """Is the service up, and has the model been downloaded yet?"""
    import detector

    loaded = detector._model is not None
    return jsonify({
        "ok": True,
        "detector_model": config.DETECTOR_MODEL,
        "detector_loaded": loaded,
        "rate_limiting": config.RATE_LIMITING_ENABLED,
        "log_entries": len(audit.read_entries()),
        "run_log": str(config.RUN_LOG.name),
        "run_log_entries": len(runlog.read_entries()),
    })


# ── YOU BUILD THIS ────────────────────────────────────────────────────────────

@app.post("/submit")
@limiter.limit(f"{config.RATE_LIMIT_PER_MINUTE}/minute;{config.RATE_LIMIT_PER_DAY}/day")
def submit():
    """
    Take a piece of text, decide about it, log the decision, answer.
    ← TODO — Milestones 3, 4 and 5

    Expects JSON:
        {"text": "...", "creator_id": "..."}

    Should return JSON with, at minimum:
        {"content_id": "...", "guess": "...", "confidence": 0.0, "label": "...",
         "model_score": 0.0, "style_score": 0.0}

    ⚠️ **Both signal scores go in the response, not just the log.** Unit 8's
    `run_attacks.py` and `run_eval.py` read `model_score` and `style_score`
    straight off this response and put them in your reports. Leave them out and
    every row of next unit's evidence says `null` — which is exactly the
    diagnostic you need to name a stage and a mechanism. You do not want to
    find that out after running the attack set.

    ─────────────────────────────────────────────────────────────────────────
    Build it in three passes. Do not skip ahead — the ordering is how you tell
    a broken route from a broken signal.

    **Milestone 3 — the route answers.**
      1. Return a hardcoded response. Confirm `curl` gets it back before you
         add any logic at all.
      2. Then pull `text` and `creator_id` out of the payload.
      3. Then call ONE signal — `detector.model_signal(text)` — and put the
         real number in. Leave confidence and label as placeholders.
      4. Log every submission with `audit.log_decision(...)`. The content_id
         matters: `/appeal` needs it, and a student who skips it rebuilds this
         whole flow later.

    **Milestone 4 — the second signal and the score.**
      5. Add `stylometry.style_signal(text)`.
      6. Combine them with `scoring.combine_signals(...)`.
      7. Log BOTH signal scores alongside the combined one, and put them in the
         response too. Next unit you can't diagnose anything without them.

    **Milestone 5 — the label.**
      8. `scoring.score_to_label(...)` and put the real label in the response.

    ─────────────────────────────────────────────────────────────────────────
    Worth deciding early, because unit 8's attack set will decide it for you:
    what should this do when `text` is missing, empty, or enormous? A crash on
    a malformed input is one of the most common real failures there is.
    """
    return _run_view("/submit", _submit_impl)


@app.post("/appeal")
def appeal():
    """
    A writer says you got it wrong. ← TODO — Milestone 5

    Expects JSON:
        {"content_id": "...", "reasoning": "..."}

    Should:
      1. Check the content_id actually exists — `audit.entries_for(id)` tells
         you. A typo here fails silently and looks like a broken endpoint,
         which is the single most common way this milestone eats an hour.
      2. Record the appeal with `audit.log_appeal(...)`, which moves the item
         to `under_review`.
      3. Confirm to the writer. No automatic re-checking needed.

    This is the smallest endpoint in the project and the one that matters most
    to the person on the other end. It's the only thing standing between a
    wrong accusation and nothing at all.
    """
    return _run_view("/appeal", _appeal_impl)


# ── Already works ─────────────────────────────────────────────────────────────

@app.get("/log")
def get_log():
    """
    The audit log, most recent last.

        curl "http://127.0.0.1:5000/log?limit=10"

    You need this in unit 8 to paste entries into your README, and you need it
    now to see whether your logging is actually working.
    """
    limit = request.args.get("limit", type=int)
    entries = audit.read_entries(limit=limit)
    return jsonify({"count": len(entries), "entries": entries})


def _blank_input() -> dict:
    return {
        "creator_id": None,
        "text_excerpt": None,
        "text_chars": None,
        "letter_ratio": None,
    }


def _public_output(status_code: int, output: dict) -> dict:
    """What the run log keeps. HTTP status lives here; the body keeps its own fields."""
    view = {"status": status_code}
    if "error" in output:
        view["error"] = output.get("error")
        return view
    for key in ("guess", "content_id", "combined_score"):
        if key in output:
            view[key] = output[key]
    if output.get("status"):
        view["app_status"] = output["status"]
    return view


def _run_view(route: str, impl):
    """Time the handler, log the record, then answer. Failures get a record too."""
    started = time.perf_counter()
    recorded = _blank_input()
    status_code = 500
    output = {"error": "internal_error"}
    try:
        status_code, output = impl(recorded)
    except Exception as exc:
        status_code = 500
        output = {"error": "internal_error", "message": type(exc).__name__}
        audit.log_rejection(
            creator_id=recorded.get("creator_id") or "unknown",
            reason="internal_error",
            detail=type(exc).__name__,
        )
    duration_ms = round((time.perf_counter() - started) * 1000, 1)
    runlog.log_run(route, recorded, _public_output(status_code, output), duration_ms)
    return jsonify(output), status_code


def _remember_text(recorded: dict, text, creator_id=None) -> None:
    if isinstance(creator_id, str) and creator_id.strip():
        recorded["creator_id"] = creator_id.strip()
    if isinstance(text, str):
        recorded["text_excerpt"] = text[:200]
        recorded["text_chars"] = len(text)


def _submit_impl(recorded: dict):
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        audit.log_rejection(creator_id="unknown", reason="invalid_json")
        return 400, {"error": "invalid_json", "message": "Body must be a JSON object."}

    creator_id = payload.get("creator_id")
    text = payload.get("text")
    _remember_text(recorded, text, creator_id if isinstance(creator_id, str) else None)

    if not isinstance(creator_id, str) or not creator_id.strip():
        audit.log_rejection(creator_id="unknown", reason="missing_creator_id")
        return 400, {"error": "missing_creator_id"}
    creator_id = creator_id.strip()
    recorded["creator_id"] = creator_id

    if text is None or not isinstance(text, str) or not text.strip():
        audit.log_rejection(creator_id=creator_id, reason="missing_or_empty_text")
        return 400, {"error": "missing_or_empty_text"}

    if len(text) > config.MAX_TEXT_CHARS:
        text = text[: config.MAX_TEXT_CHARS]
        _remember_text(recorded, text, creator_id)

    if len(text.strip()) < config.MIN_TEXT_CHARS:
        audit.log_rejection(creator_id=creator_id, reason="text_too_short")
        return 400, {
            "error": "text_too_short",
            "message": f"Need at least {config.MIN_TEXT_CHARS} characters to score.",
        }

    ratio = writing_check.letter_ratio(text)
    recorded["letter_ratio"] = round(ratio, 4)
    if not writing_check.is_writing(text):
        audit.log_rejection(
            creator_id=creator_id,
            reason="not_writing",
            letter_ratio=round(ratio, 4),
        )
        return 400, {
            "error": "not_writing",
            "message": "This submission does not contain enough letters to score as writing.",
            "letter_ratio": round(ratio, 4),
        }

    content_id = str(uuid.uuid4())

    try:
        model_score = detector.model_signal(text)
    except detector.DetectorUnavailable as exc:
        audit.log_rejection(
            creator_id=creator_id,
            reason="detector_unavailable",
            detail=str(exc),
            content_id=content_id,
        )
        return 503, {"error": "detector_unavailable", "message": str(exc)}
    except ValueError as exc:
        audit.log_rejection(creator_id=creator_id, reason="text_too_short", detail=str(exc))
        return 400, {"error": "text_too_short", "message": str(exc)}

    style_score = stylometry.style_signal(text)
    combined = scoring.combine_signals(model_score, style_score)
    guess, label = scoring.score_to_label(combined)

    audit.log_decision(
        content_id=content_id,
        creator_id=creator_id,
        guess=guess,
        model_score=model_score,
        style_score=style_score,
        combined_score=combined,
        label=label,
        status="decided",
    )

    return 200, {
        "content_id": content_id,
        "guess": guess,
        "confidence": combined,
        "label": label,
        "model_score": model_score,
        "style_score": style_score,
        "combined_score": combined,
    }


def _appeal_impl(recorded: dict):
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        audit.log_rejection(creator_id="unknown", reason="invalid_json")
        return 400, {"error": "invalid_json"}

    content_id = payload.get("content_id")
    reasoning = payload.get("reasoning")
    if isinstance(content_id, str):
        recorded["content_id"] = content_id.strip()
    _remember_text(recorded, reasoning if isinstance(reasoning, str) else None)

    if not isinstance(content_id, str) or not content_id.strip():
        audit.log_rejection(creator_id="unknown", reason="missing_content_id")
        return 400, {"error": "missing_content_id"}
    content_id = content_id.strip()
    recorded["content_id"] = content_id

    if not isinstance(reasoning, str) or not reasoning.strip():
        audit.log_rejection(creator_id="unknown", reason="missing_reasoning")
        return 400, {"error": "missing_reasoning"}

    prior = audit.entries_for(content_id)
    decision = next((e for e in prior if e.get("guess") is not None), None)
    if decision is None:
        audit.log_rejection(
            creator_id="unknown",
            reason="unknown_content_id",
            content_id=content_id,
        )
        return 404, {
            "error": "unknown_content_id",
            "message": "No submission with that content_id appears in the audit log.",
        }

    creator_id = decision.get("creator_id", "unknown")
    recorded["creator_id"] = creator_id
    entry = audit.log_appeal(content_id, creator_id, reasoning.strip())

    return 200, {
        "ok": True,
        "content_id": content_id,
        "status": "under_review",
        "message": "Your appeal was recorded. A reviewer will look at this submission.",
        "appeal_logged_at": entry.get("timestamp"),
    }


def main():
    print(f"Provenance Guard on http://{config.HOST}:{config.PORT}")
    print(f"  detector model:  {config.DETECTOR_MODEL}")
    print(f"  rate limiting:   {'ON' if config.RATE_LIMITING_ENABLED else 'off (unit 8)'}")
    print(f"  audit log:       {config.AUDIT_LOG}")
    print(f"  run log:         {config.RUN_LOG}")
    print()
    print("Check it's alive:")
    print(f'  curl -X POST http://{config.HOST}:{config.PORT}/ping \\')
    print('    -H "Content-Type: application/json" \\')
    print("    -d '{\"message\": \"hello\"}'")
    print()
    # debug=True hands out an interactive debugger, so it's local-only — see config.py
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)


if __name__ == "__main__":
    main()
