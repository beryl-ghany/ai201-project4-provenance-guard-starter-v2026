# Capstone Run Log — stretch

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
  "elapsed_ms": 4087.56,
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
  "elapsed_ms": 48.16,
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
  "elapsed_ms": 44.57,
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
  "min_ms": 30.95,
  "max_ms": 116.03,
  "avg_ms": 37.79,
  "p95_ms": 116.03,
  "passed": true
}
```

**Trial 2**

```json
{
  "total_requests": 20,
  "under_3s_count": 20,
  "pct_under_3s": 100.0,
  "min_ms": 34.79,
  "max_ms": 47.72,
  "avg_ms": 41.21,
  "p95_ms": 47.72,
  "passed": true
}
```

**Trial 3**

```json
{
  "total_requests": 20,
  "under_3s_count": 20,
  "pct_under_3s": 100.0,
  "min_ms": 38.17,
  "max_ms": 126.01,
  "avg_ms": 48.57,
  "p95_ms": 126.01,
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
    "timestamp": "2026-11-19T00:14:57.211+00:00",
    "request_id": "9cb16696",
    "input_length": 62,
    "model_latency_ms": 42.21,
    "style_latency_ms": 0.05,
    "combine_latency_ms": 0.01,
    "total_latency_ms": 42.54,
    "outcome": "success",
    "degraded_mode": false,
    "error_stage": null,
    "error_message": null,
    "stages": {
      "model_signal": 42.21,
      "style_signal": 0.05,
      "combine": 0.01
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
    "timestamp": "2026-11-19T00:14:57.450+00:00",
    "request_id": "ec6a6aea",
    "input_length": 62,
    "model_latency_ms": 42.37,
    "style_latency_ms": 0.04,
    "combine_latency_ms": 0.0,
    "total_latency_ms": 42.65,
    "outcome": "success",
    "degraded_mode": false,
    "error_stage": null,
    "error_message": null,
    "stages": {
      "model_signal": 42.37,
      "style_signal": 0.04,
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
    "timestamp": "2026-11-19T00:14:57.587+00:00",
    "request_id": "f12616da",
    "input_length": 62,
    "model_latency_ms": 42.85,
    "style_latency_ms": 0.04,
    "combine_latency_ms": 0.0,
    "total_latency_ms": 43.15,
    "outcome": "success",
    "degraded_mode": false,
    "error_stage": null,
    "error_message": null,
    "stages": {
      "model_signal": 42.85,
      "style_signal": 0.04,
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

  - Average request latency: 37.31ms (p50)
  - 95th percentile: 84.21ms
  - Total logged requests: 81

### Latency Breakdown (Stretch Goal B)

| Stage | Avg (ms) | Min (ms) | Max (ms) | % of Total |
|-------|----------|----------|----------|------------|
| combine | 0.0 | 0.0 | 0.01 | 0.0% |
| model_signal | 89.77 | 26.89 | 4083.25 | 99.9% |
| style_signal | 0.12 | 0.04 | 0.33 | 0.1% |

**For 100 users/day at ~5 requests each (500 requests/day):**
- Assuming 2 seconds average per request
- Total compute time: 500 × 2s = 1000 seconds ≈ 17 minutes/day
- Monthly: 17 min × 30 = 8.5 hours compute time
