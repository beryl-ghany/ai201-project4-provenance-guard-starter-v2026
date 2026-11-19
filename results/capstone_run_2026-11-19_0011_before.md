# Capstone Run Log — before

- Produced by: `run_capstone_eval.py`
- 3 trials per criterion · 2026-11-19 00:11

## Summary

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 6. Timeout handling | — | PASS | PASS | PASS | MET |
| 7. Retry success | — | PASS | PASS | PASS | MET |
| 8. Graceful degradation | — | PASS | PASS | PASS | MET |
| 9. Latency target | — | PASS | PASS | PASS | MET |
| 10. Error logging | — | PASS | PASS | PASS | MET |

---

## Detailed Results

### 6. Timeout handling

**Trial 1**

```json
{
  "status": 200,
  "elapsed_ms": 10004.43,
  "within_12s": true,
  "has_degraded_field": true,
  "degraded": true,
  "guess": "unsure",
  "passed": true
}
```

**Trial 2**

```json
{
  "status": 200,
  "elapsed_ms": 788.88,
  "within_12s": true,
  "has_degraded_field": true,
  "degraded": false,
  "guess": "human",
  "passed": true
}
```

**Trial 3**

```json
{
  "status": 200,
  "elapsed_ms": 40.24,
  "within_12s": true,
  "has_degraded_field": true,
  "degraded": false,
  "guess": "human",
  "passed": true
}
```

### 7. Retry success

**Trial 1**

```json
{
  "status": 200,
  "has_error_field": false,
  "has_guess": true,
  "no_retry_exposure": true,
  "passed": true
}
```

**Trial 2**

```json
{
  "status": 200,
  "has_error_field": false,
  "has_guess": true,
  "no_retry_exposure": true,
  "passed": true
}
```

**Trial 3**

```json
{
  "status": 200,
  "has_error_field": false,
  "has_guess": true,
  "no_retry_exposure": true,
  "passed": true
}
```

### 8. Graceful degradation

**Trial 1**

```json
{
  "status": 200,
  "guess": "human",
  "label": "This looks like it was written by a person. We are...",
  "degraded": false,
  "has_valid_guess": true,
  "has_valid_label": true,
  "passed": true
}
```

**Trial 2**

```json
{
  "status": 200,
  "guess": "human",
  "label": "This looks like it was written by a person. We are...",
  "degraded": false,
  "has_valid_guess": true,
  "has_valid_label": true,
  "passed": true
}
```

**Trial 3**

```json
{
  "status": 200,
  "guess": "human",
  "label": "This looks like it was written by a person. We are...",
  "degraded": false,
  "has_valid_guess": true,
  "has_valid_label": true,
  "passed": true
}
```

### 9. Latency target

**Trial 1**

```json
{
  "total_requests": 20,
  "under_3s_count": 20,
  "pct_under_3s": 100.0,
  "min_ms": 27.29,
  "max_ms": 56.15,
  "avg_ms": 33.48,
  "p95_ms": 56.15,
  "passed": true
}
```

**Trial 2**

```json
{
  "total_requests": 20,
  "under_3s_count": 20,
  "pct_under_3s": 100.0,
  "min_ms": 27.53,
  "max_ms": 61.5,
  "avg_ms": 30.7,
  "p95_ms": 61.5,
  "passed": true
}
```

**Trial 3**

```json
{
  "total_requests": 20,
  "under_3s_count": 20,
  "pct_under_3s": 100.0,
  "min_ms": 27.28,
  "max_ms": 36.98,
  "avg_ms": 29.01,
  "p95_ms": 36.98,
  "passed": true
}
```

### 10. Error logging

**Trial 1**

```json
{
  "total_log_entries": 1,
  "has_structured_format": true,
  "has_request_tracking": true,
  "has_outcome_field": false,
  "error_timeout_entries": 1,
  "success_entries": 0,
  "sample_entry": {
    "timestamp": "2026-11-19T00:11:39.586+00:00",
    "event": "timeout",
    "stage": "model_signal",
    "message": "Timeout after 10001ms",
    "request_id": "fdda25fc",
    "duration_ms": 10000.65
  },
  "passed": true
}
```

**Trial 2**

```json
{
  "total_log_entries": 1,
  "has_structured_format": true,
  "has_request_tracking": true,
  "has_outcome_field": false,
  "error_timeout_entries": 1,
  "success_entries": 0,
  "sample_entry": {
    "timestamp": "2026-11-19T00:11:39.586+00:00",
    "event": "timeout",
    "stage": "model_signal",
    "message": "Timeout after 10001ms",
    "request_id": "fdda25fc",
    "duration_ms": 10000.65
  },
  "passed": true
}
```

**Trial 3**

```json
{
  "total_log_entries": 1,
  "has_structured_format": true,
  "has_request_tracking": true,
  "has_outcome_field": false,
  "error_timeout_entries": 1,
  "success_entries": 0,
  "sample_entry": {
    "timestamp": "2026-11-19T00:11:39.586+00:00",
    "event": "timeout",
    "stage": "model_signal",
    "message": "Timeout after 10001ms",
    "request_id": "fdda25fc",
    "duration_ms": 10000.65
  },
  "passed": true
}
```

---

## Cost Calculation

- **API cost**: $0 (local model, no external API calls)
- **Compute cost per run**: Measured average latency × requests


**For 100 users/day at ~5 requests each (500 requests/day):**
- Assuming 2 seconds average per request
- Total compute time: 500 × 2s = 1000 seconds ≈ 17 minutes/day
- Monthly: 17 min × 30 = 8.5 hours compute time
