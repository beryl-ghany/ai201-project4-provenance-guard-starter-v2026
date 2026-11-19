# Capstone Run Log — after2

- Produced by: `run_capstone_eval.py`
- 3 trials per criterion · 2026-11-19 00:13

## Summary

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 6. Timeout handling | — | PASS | PASS | PASS | MET |
| 7. Retry success | — | PASS | PASS | PASS | MET |
| 8. Graceful degradation | — | PASS | PASS | PASS | MET |
| 9. Latency target | — | PASS | PASS | PASS | MET |
| 10. Error logging | — | MISS | MISS | MISS | MISSED |

---

## Detailed Results

### 6. Timeout handling

**Trial 1**

```json
{
  "status": 200,
  "elapsed_ms": 3566.66,
  "within_12s": true,
  "has_degraded_field": true,
  "degraded": false,
  "guess": "human",
  "passed": true
}
```

**Trial 2**

```json
{
  "status": 200,
  "elapsed_ms": 38.29,
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
  "elapsed_ms": 37.58,
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
  "min_ms": 24.26,
  "max_ms": 30.54,
  "avg_ms": 26.83,
  "p95_ms": 30.54,
  "passed": true
}
```

**Trial 2**

```json
{
  "total_requests": 20,
  "under_3s_count": 20,
  "pct_under_3s": 100.0,
  "min_ms": 25.73,
  "max_ms": 118.56,
  "avg_ms": 32.23,
  "p95_ms": 118.56,
  "passed": true
}
```

**Trial 3**

```json
{
  "total_requests": 20,
  "under_3s_count": 20,
  "pct_under_3s": 100.0,
  "min_ms": 25.06,
  "max_ms": 96.29,
  "avg_ms": 32.2,
  "p95_ms": 96.29,
  "passed": true
}
```

### 10. Error logging

**Trial 1**

```json
{
  "total_log_entries": 0,
  "has_structured_format": false,
  "has_request_tracking": false,
  "error_timeout_entries": 0,
  "success_entries": 0,
  "degraded_entries": 0,
  "sample_entry": null,
  "passed": false
}
```

**Trial 2**

```json
{
  "total_log_entries": 0,
  "has_structured_format": false,
  "has_request_tracking": false,
  "error_timeout_entries": 0,
  "success_entries": 0,
  "degraded_entries": 0,
  "sample_entry": null,
  "passed": false
}
```

**Trial 3**

```json
{
  "total_log_entries": 0,
  "has_structured_format": false,
  "has_request_tracking": false,
  "error_timeout_entries": 0,
  "success_entries": 0,
  "degraded_entries": 0,
  "sample_entry": null,
  "passed": false
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
