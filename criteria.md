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

## Capstone Criteria

The following criteria evaluate the Shape B failure-hardening extension.

---

## 6. Timeout handling returns within 12 seconds with degraded flag

When model inference exceeds 10 seconds (simulated or real), the response
returns within 12 seconds total with `degraded: true` in the JSON.

**Why this target:** A stuck model must not hang the user indefinitely. Returning
in bounded time with a degraded flag lets the caller decide whether to retry or
accept an uncertain result.

---

## 7. Transient failures that succeed on retry do not expose errors

When a transient failure (e.g., temporary resource contention) is resolved on
retry, the caller receives a normal 200 response with no error field.

**Why this target:** Retry logic should mask intermittent failures from the user.
Exposing internal retry mechanics leaks implementation details and confuses callers.

---

## 8. Graceful degradation returns valid guess/label defaulting to unsure

In degraded mode (model unavailable or timed out), the response includes a valid
`guess` field (defaults to "unsure") and a corresponding `label` string.

**Why this target:** Even when the model cannot run, the service must return a
complete response shape. The unsure label is the safest default—neither accusation
nor clearance.

---

## 9. 95% of warm requests complete under 3 seconds

After the model is loaded, at least 19 of 20 consecutive requests complete
within 3000 milliseconds.

**Why this target:** Latency above 3 seconds feels broken to a user waiting for
feedback. The first cold request is excluded because model loading is unavoidable.

---

## 10. Every timeout or error leaves a structured log entry

When a timeout or error occurs, the audit log contains an entry with `event: "error"`
or `event: "timeout"`, the stage where it happened, and the duration in milliseconds.

**Why this target:** Silent failures are invisible failures. Structured logs are
the only way to diagnose production issues after the fact.
