# Capstone Run Log — after3

- Produced by: `run_capstone_eval.py`
- 3 trials per criterion · 2026-11-19 00:14

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
  "elapsed_ms": 41.64,
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
  "elapsed_ms": 43.8,
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
  "elapsed_ms": 39.08,
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
  "min_ms": 25.19,
  "max_ms": 83.35,
  "avg_ms": 30.09,
  "p95_ms": 83.35,
  "passed": true
}
```

**Trial 2**

```json
{
  "total_requests": 20,
  "under_3s_count": 20,
  "pct_under_3s": 100.0,
  "min_ms": 25.68,
  "max_ms": 31.1,
  "avg_ms": 27.56,
  "p95_ms": 31.1,
  "passed": true
}
```

**Trial 3**

```json
{
  "total_requests": 20,
  "under_3s_count": 20,
  "pct_under_3s": 100.0,
  "min_ms": 25.51,
  "max_ms": 108.88,
  "avg_ms": 32.49,
  "p95_ms": 108.88,
  "passed": true
}
```

### 10. Error logging

**Trial 1**

```json
{
  "total_log_entries": 50,
  "has_structured_format": true,
  "has_request_tracking": true,
  "error_timeout_entries": 0,
  "success_entries": 50,
  "degraded_entries": 0,
  "sample_entry": {
    "timestamp": "2026-11-19T00:14:04.699+00:00",
    "request_id": "bf259b05",
    "input_length": 62,
    "model_latency_ms": 26.86,
    "style_latency_ms": 0.03,
    "combine_latency_ms": 0.0,
    "total_latency_ms": 27.09,
    "outcome": "success",
    "degraded_mode": false,
    "error_stage": null,
    "error_message": null,
    "stages": {
      "model_signal": 26.86,
      "style_signal": 0.03,
      "combine": 0.0
    }
  },
  "passed": true
}
```

**Trial 2**

```json
{
  "total_log_entries": 50,
  "has_structured_format": true,
  "has_request_tracking": true,
  "error_timeout_entries": 0,
  "success_entries": 50,
  "degraded_entries": 0,
  "sample_entry": {
    "timestamp": "2026-11-19T00:14:04.793+00:00",
    "request_id": "37cb2034",
    "input_length": 62,
    "model_latency_ms": 26.8,
    "style_latency_ms": 0.03,
    "combine_latency_ms": 0.0,
    "total_latency_ms": 27.01,
    "outcome": "success",
    "degraded_mode": false,
    "error_stage": null,
    "error_message": null,
    "stages": {
      "model_signal": 26.8,
      "style_signal": 0.03,
      "combine": 0.0
    }
  },
  "passed": true
}
```

**Trial 3**

```json
{
  "total_log_entries": 50,
  "has_structured_format": true,
  "has_request_tracking": true,
  "error_timeout_entries": 0,
  "success_entries": 50,
  "degraded_entries": 0,
  "sample_entry": {
    "timestamp": "2026-11-19T00:14:04.887+00:00",
    "request_id": "4e137e39",
    "input_length": 62,
    "model_latency_ms": 26.95,
    "style_latency_ms": 0.03,
    "combine_latency_ms": 0.0,
    "total_latency_ms": 27.16,
    "outcome": "success",
    "degraded_mode": false,
    "error_stage": null,
    "error_message": null,
    "stages": {
      "model_signal": 26.95,
      "style_signal": 0.03,
      "combine": 0.0
    }
  },
  "passed": true
}
```

---

## Cost Calculation

- **API cost**: $0 (local model, no external API calls)
- **Compute cost per run**: Measured average latency × requests

  - Average request latency: 24.84ms (p50)
  - 95th percentile: 35.3ms
  - Total logged requests: 81

### Latency Breakdown (Stretch Goal B)

| Stage | Avg (ms) | Min (ms) | Max (ms) | % of Total |
|-------|----------|----------|----------|------------|
| combine | 0.0 | 0.0 | 0.01 | 0.0% |
| model_signal | 27.23 | 23.02 | 105.29 | 99.7% |
| style_signal | 0.09 | 0.03 | 0.17 | 0.3% |

**For 100 users/day at ~5 requests each (500 requests/day):**
- Assuming 2 seconds average per request
- Total compute time: 500 × 2s = 1000 seconds ≈ 17 minutes/day
- Monthly: 17 min × 30 = 8.5 hours compute time
