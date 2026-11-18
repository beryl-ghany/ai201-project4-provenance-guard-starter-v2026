# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** the build was scored against them.

---

## 1. At most 1 of 10 pieces I wrote myself is labeled high-confidence AI

On ten short pieces I wrote without AI help, at most one may receive the
high-confidence AI label (`guess` is `ai` and combined score is at least 0.65).

**Why this target:** On a writing site, a false accusation is the expensive
mistake. One in ten wrong flags is already harsh from a writer's point of view,
but it gives me room for plain, predictable prose that my model signal misreads.

---

## 2. Clearly AI and clearly human samples differ by at least 0.25 combined score

On my four calibration texts (clearly AI, clearly human, plain human, lightly
edited AI), the highest and lowest combined scores must be at least 0.25 apart.

**Why this target:** If everything lands in a narrow band, the two signals and
weights are not separating anything, and the labels are cosmetic. A quarter-point
spread is modest but observable on the same machine.

---

## 3. Each of the three reader labels is reachable on at least one submission

For high-confidence human, unsure, and high-confidence AI, there exists at least
one submitted text whose response uses that label.

**Why this target:** A label nobody ever sees is not a product decision — it is
dead code. Milestone 5 requires me to prove each band is reachable with real POSTs.

---

## 4. Every valid appeal moves status to under_review and appends a log entry

For any `content_id` that already has a decision row in `logs/audit.jsonl`, POST
`/appeal` returns success, and the next log line for that id has
`status: "under_review"` and an `event: "appeal"` with the writer's reasoning.

**Why this target:** The appeal path is the only recovery when the system is wrong.
If it does not always log and change status, a writer has no evidence they pushed back.

---

## 5. Missing or empty text returns HTTP 400 and does not write a decision row

When `text` is missing, null, or only whitespace, POST `/submit` returns 400 with
an error field, and no new entry with a `guess` field is appended to the audit log
for that request.

**Why this target:** Bad input is normal at the edge. Crashing or logging a fake
decision on empty bodies would pollute the audit trail I need in unit 8 to diagnose attacks.

---

# Capstone criteria

These five are for the capstone extension. They were written before any capstone
trial. The five above are the unit 7 criteria and stay as they were.

Letter ratio, where a criterion depends on it, means the count of Unicode letters
(`str.isalpha`) divided by `len(text)`, on the string posted.

The five non-writing strings:

1. `!!! ??? ... ,,, ;;; --- ((( )))`
2. `🙂🙃😀😃😄😁😆😅😂🤣` repeated three times (30 emoji)
3. `#### $$$$ %%%% ^^^^ &&&& **** #### $$$$`
4. `1234567890 1234567890 1234567890 1234567890`
5. `---- ____ .... **** ~~~~ ++++ ==== ####`

The five ordinary paragraphs:

1. `I stayed up until two finishing this draft. My sentences jump from three words to a whole line, and I keep changing the ending.`
2. `The tap was dripping again. I put a bowl under it, missed, and spent the next ten minutes chasing water across the counter with a towel.`
3. `We got to the platform as the doors were closing. Maya yelled for me to wait, then laughed because she had the tickets and I had the snacks.`
4. `Chapter notes from Tuesday: the argument turns on one example, the harbor, and I still do not think the second paragraph earns that turn.`
5. `Dear building manager, the hallway light on the third floor has been out since Monday. I carried groceries up in the dark and nearly missed a step.`

The latency paragraph:

`I wrote this paragraph so a warm request would have something ordinary to score. It is about a walk to the store in the rain, a torn grocery bag, and the orange that rolled into the street. None of that is a calibration trick. It is just long enough that the model has a few sentences to read, and short enough that I can paste it into a log without filling the page.`

Each submit in a trial uses its own `creator_id`, so the per-creator rate limit is not what these criteria measure.

---

## 1. All five non-writing strings return HTTP 400, `not_writing`, and no guess

POST `/submit` once with each of the five non-writing strings above. All five
responses are HTTP 400, the JSON `error` field is exactly `not_writing`, and the
JSON has no `guess` key.

**Target:** 5 of 5.

**Why this target:** A symbol string, an emoji run, or a digit run is long enough
to pass the old 20-character check and still is not a piece of writing. Scoring it
produces a label nobody wrote. All five have to fail closed; four of five would
leave a known bad body getting a verdict. The ratio floor is 0.40 because normal
prose in this service, spaces included, sits around 0.75, and these five sit near 0.
A floor of 0.70 would start rejecting short notes that are mostly numbers and names.

**What would fail it:** Any of the five comes back 200, 500, a different `error`
string, or a body that includes `guess`.

---

## 2. None of those five refusals append an audit row that has a guess

For each of the same five posts, take the audit log length before the post and
read only the lines appended by that post. None of those new lines has a `guess`
field.

**Target:** 5 of 5.

**Why this target:** A 400 that still writes a decision row leaves a label in the
audit for text the route claims it refused. The appeal path and the unit 8
attack read that file. One leaked guess is enough to make the refusal a lie.
Counting new lines, rather than the whole file, keeps older decisions from
changing the score.

**What would fail it:** A new audit line from one of the five posts contains `guess`.

---

## 3. Each of those five refusals appends one run record, and the handler finishes in under 200 ms

For each of the same five posts, exactly one new JSON object is appended to
`logs/runs.jsonl`. That object has `timestamp` (string), `input` (object),
`output.status` equal to 400, `output.error` equal to `not_writing`, and
`duration_ms` as a number strictly under 200. `duration_ms` is the handler time
stored in that record, not a separate clock.

**Target:** 5 of 5.

**Why this target:** The refusal is only real if it is visible later and if it
returns before the model runs. A warm GPT-2 score on this machine is on the order
of a second, so 200 ms is too short for a path that accidentally called
`detector.model_signal` and long enough for a JSON parse plus one file append.
A cap of 20 ms would fail on a slow disk without telling me the model ran.
Missing the record fails the same criterion, because a refusal that is only an
absence cannot be diagnosed.

**What would fail it:** No new line, more than one new line, a missing field, a
status other than 400, or `duration_ms` of 200 or more.

---

## 4. The five ordinary paragraphs still return HTTP 200 with a guess and both scores

POST `/submit` once with each ordinary paragraph above. Every response is HTTP 200
and the JSON has `guess` as a string, `model_score` as a number, and `style_score`
as a number.

**Target:** 5 of 5.

**Why this target:** The gate is a failure path in front of a system that already
scored prose. If any of these five is rejected, the extension broke the original
job. These five are all above a 0.60 letter ratio, well clear of the 0.40 floor,
so a miss here is the gate or the route, not a borderline ratio. I am not
requiring a particular label: the old criteria already cover that, and this one
only checks that a real paragraph is still scored.

**What would fail it:** Any paragraph returns a status other than 200, or the
body is missing `guess`, `model_score`, or `style_score`.

---

## 5. After the model is loaded, 9 of 10 sequential warm submits of the latency paragraph return within 3 seconds

GET `/health` and confirm `detector_loaded` is true. If it is false, send one
submit of the latency paragraph, wait until it returns, and confirm `/health`
again. Then send 10 more sequential POSTs of that same paragraph, each with its
own `creator_id`. At least 9 of those 10 return HTTP 200, and the client time
from send to full response is 3000 ms or less. A 429 or a 500 counts as not
meeting the bar for that call.

**Target:** 9 of 10.

**Why this target:** The project notes put a warm score at about one to two
seconds on CPU. Three seconds is just outside that, so a handler that reloads
GPT-2 on every request (ten seconds and up) misses, and a normal warm score
does not. One second would fail a correct run on this CPU. Nine of ten allows
a single scheduling stall; two stalls means the warm path is not actually warm.
The load that happens before `detector_loaded` is true is outside this criterion
on purpose: that wait is process start, not one pass.

**What would fail it:** Two or more of the ten calls take over 3000 ms, or return
a status other than 200.
