# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

Provenance Guard is a small backend a writing site could call when someone posts text. It does not claim certainty; it returns a guess, a score, and plain-English label text, plus a way to appeal.

Path from POST to label:

1. **POST /submit** receives JSON with `text` and `creator_id`. The route rejects missing or empty text with HTTP 400.
2. **Signal one** (`detector.model_signal`) runs the local GPT-2 model and scores how predictable the wording is (higher → more AI-like).
3. **Signal two** (`stylometry.style_signal`) measures sentence-length spread, vocabulary repetition, and punctuation density (higher → more AI-like).
4. **Combine** (`scoring.combine_signals`) merges the two scores with weights from `config.py`, pulling toward 0.5 when they disagree sharply.
5. **Label** (`scoring.score_to_label`) maps the combined score to one of three reader-facing sentences using thresholds in `config.py`.
6. **Audit** (`audit.log_decision`) appends a JSON line to `logs/audit.jsonl` with both signal scores and the label.
7. The HTTP response returns `content_id`, `guess`, `confidence`, `label`, `model_score`, and `style_score` so the site can show the label and store the id for appeals.

If the writer disagrees, **POST /appeal** with `content_id` and `reasoning` appends an appeal event and sets status to `under_review` without re-running the detector.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** Perplexity under GPT-2 — how predictable each next token is. Low surprise becomes a high `model_score` (more AI-like).

**Why that might differ between human and AI writing:** Models tend to produce fluent, common phrasing; human drafts can be odd, specific, or rough.

**What it can't see:** Authorship. Plain, careful human prose (ESL writers, short sentences, simple vocabulary) can look as predictable as generated text. Ornate rare words can look “human” even when a model wrote them.

### Signal two — the style signal

**What it measures:** Sentence-length coefficient of variation, type-token ratio, and punctuation density, combined into one 0–1 score in `stylometry.style_signal`.

**Why that might differ between human and AI writing:** Generated prose often marches in even sentence lengths with steady vocabulary; human drafts jump from three-word sentences to long ones.

**What it can't see:** Meaning. Typos, pasted quotes, or manual line breaks change the shape without changing who wrote the argument — a cheap evasion path in unit 8.

### The combining rule

**The rule:** Start with a weighted average of the two signals (both oriented so higher = more AI-like). If the two scores differ by more than 0.35, blend the average toward 0.5 — disagreement becomes uncertainty instead of a confident wrong side.

**The numbers:** `WEIGHT_MODEL_SIGNAL = 0.55`, `WEIGHT_STYLE_SIGNAL = 0.45`. Disagreement pull: up to 0.25 toward 0.5 when gap exceeds 0.35. Label thresholds: human ≤ 0.35, AI ≥ 0.65, unsure between.

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:** On my sample human paragraph, `model_score` was 0.45 (borderline predictable) but `style_score` was 0.14 (lumpy, human-shaped). The weighted average landed at 0.31 — human label — instead of averaging to a false “unsure” band.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | This looks like it was written by a person. We are not treating it as AI-generated. |
| unsure | 0.35 – 0.65 | We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong. |
| high-confidence AI | 0.65 – 1.00 | This text looks like it was mostly produced by an AI writing tool rather than written directly by a person. |

**Why I worded the "unsure" one this way:** It states uncertainty without calling the writer a cheater, and it points to the appeal path instead of leaving them stuck with a silent score.

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
curl.exe -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"text\": \"I stayed up until two finishing this draft. My sentences are all over the place — some tiny, some way too long — and I keep changing my mind mid-paragraph about whether the ending works. Nobody asked me to write it; I just needed to get it out.\", \"creator_id\": \"creator_beryl_01\"}"
```

```json
{
  "combined_score": 0.3107,
  "confidence": 0.3107,
  "content_id": "90acb9c9-2204-46e2-8241-dbf7577bb2e6",
  "guess": "human",
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "model_score": 0.4511,
  "style_score": 0.1391
}
```

**An appeal**

```bash
curl.exe -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" -d "{\"content_id\": \"90acb9c9-2204-46e2-8241-dbf7577bb2e6\", \"reasoning\": \"I wrote every word myself at my kitchen table; please have a person review.\"}"
```

```json
{
  "appeal_logged_at": "2026-11-02T02:22:02+00:00",
  "content_id": "90acb9c9-2204-46e2-8241-dbf7577bb2e6",
  "message": "Your appeal was recorded. A reviewer will look at this submission.",
  "ok": true,
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
curl.exe "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 2,
  "entries": [
    {
      "timestamp": "2026-11-02T02:22:02+00:00",
      "content_id": "90acb9c9-2204-46e2-8241-dbf7577bb2e6",
      "creator_id": "creator_beryl_01",
      "guess": "human",
      "model_score": 0.4511,
      "style_score": 0.1391,
      "combined_score": 0.3107,
      "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
      "status": "decided"
    },
    {
      "timestamp": "2026-11-02T02:22:02+00:00",
      "content_id": "90acb9c9-2204-46e2-8241-dbf7577bb2e6",
      "creator_id": "creator_beryl_01",
      "event": "appeal",
      "status": "under_review",
      "reasoning": "I wrote every word myself at my kitchen table; please have a person review."
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* Whether each draft criterion in `criteria.md` could be checked by someone who could not ask me what I meant.
- *What came back:* The false-positive criterion was testable; “handles uncertainty well” was not — it had no number.
- *What I changed:* Kept the 1-in-10 false-positive cap and added explicit 400-on-empty-text and appeal-logging criteria instead of vague wording.

**Moment 2**

- *What I asked for:* Strongest reader-side reading of my three label strings, as the writer not as the engineer.
- *What came back:* The unsure label sounded like a soft accusation until it mentioned human review.
- *What I changed:* Added the sentence “You can ask for a human review if you think we got it wrong” to the unsure variant.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
