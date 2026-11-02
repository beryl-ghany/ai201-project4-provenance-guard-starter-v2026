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
