# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 19:58
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `34bc6b00-f01c-4ea9-99b1-52adcdf9019f` | human | 0.332 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `e445161b-fce5-4e9a-a69d-764e97d6d949` | unsure | 0.384 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `f6f9d94f-9338-4151-b7bf-2619fac79f69` | unsure | 0.492 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `800e79f8-97a2-424c-8af4-35c90e4cb49f` | unsure | 0.570 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c4a335ac-764c-4e50-a6b5-088e64c26351` | human | 0.220 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `79a68553-bb7c-4314-ba71-fd8dda7f80ab` | unsure | 0.378 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `6b47a5a5-3bc8-4594-844b-5935af16b326` | unsure | 0.613 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `d9cc1aa4-0606-4992-8b00-be2916efbd0f` | human | 0.317 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `0a1c87ec-3b17-4fb0-87af-1d2cec8af786` | unsure | 0.505 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `0e9b3e2d-198d-438b-9d51-154e130f6c00` | ai | 0.762 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `366c37c6-94ee-4725-85bd-d5510bd15995` | unsure | 0.472 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `a16ea845-ee60-4588-b088-387acc6af8d3` | unsure | 0.623 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `ef4a390f-5a79-4204-a4b1-6fd6b188a3d3` | unsure | 0.621 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `fe8c7e78-f504-4fbe-995e-d830879cace3` | unsure | 0.609 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `42a7923a-6830-4ff9-b5d4-c2af01b0a499` | ai | 0.661 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `b98a646f-8ddd-4871-8958-c69c28d5ff77` | unsure | 0.576 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `8908723d-58ec-4b0a-b0c0-31a3ff460bdb` | unsure | 0.570 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `3318750f-c312-4e82-a4ef-346c46cf731d` | human | 0.260 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `02b51b00-1fc2-4108-9b0a-24e0498cb2bf` | human | 0.309 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `0493c3c6-60b8-4d9d-ae11-4d6c9278bf5e` | human | 0.155 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `51a6b856-ba0b-4b4e-9973-b235caf832e5` | unsure | 0.496 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `73a9ae41-7a72-4304-bfd1-42f65ed01404` | unsure | 0.389 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `d3352c33-a7ee-4540-ad78-634bc986345f` | unsure | 0.426 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `ffc7f3a3-3964-4eca-b709-c8a31ad75381` | unsure | 0.445 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `b1787e64-f9c0-4b83-be65-385c3de221e0` | human | 0.273 |  |
| MF04 | malformed | text is only punctuation | 200 | `a4a59c73-7e4c-4b8f-9535-5fd324de0ca7` | unsure | 0.416 |  |
| MF05 | malformed | text is a very long single word | 200 | `6dcc54e6-0801-4b80-b922-2b117452a186` | ai | 0.864 |  |
| MF06 | malformed | text is emoji only | 200 | `c5812706-5ff2-429e-a86d-69a4ad87b8b8` | ai | 0.931 |  |
| MF07 | malformed | text is right-to-left script | 200 | `379e7e7d-baea-495b-9640-c6aed3e29f4a` | ai | 0.941 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `d5a117fa-6810-44ea-98be-871fd4c40359` | ai | 0.808 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9e7af23c-cd34-412d-8447-986221d7d976` | human | 0.343 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `40018f87-8365-4af0-ac80-0d3d3e7a6479` | human | 0.343 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b2d11841-bc37-4a6c-a763-1f0605f74625` | human | 0.343 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f5e79896-18c5-46a3-a4f8-dd3e8daaf618` | human | 0.343 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5d90412b-8065-4731-af64-87a8520a1693` | human | 0.343 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b6a6471d-98e2-42e7-bb34-fef08ba08012` | human | 0.343 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `933eb954-c1a5-40c2-83e4-9cca71d4a100` | human | 0.343 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `07387b64-2764-44ce-9287-9cc6682ddd3c` | human | 0.343 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ffbbc999-880e-4871-a205-8bc0e5daf778` | human | 0.343 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ccf02e52-d0ce-45bd-85f7-a9bab45fccc4` | human | 0.343 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "34bc6b00-f01c-4ea9-99b1-52adcdf9019f",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3319,
  "model_score": 0.1635,
  "style_score": 0.5339,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "e445161b-fce5-4e9a-a69d-764e97d6d949",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.3835,
  "model_score": 0.5943,
  "style_score": 0.1068,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "f6f9d94f-9338-4151-b7bf-2619fac79f69",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.4918,
  "model_score": 0.6662,
  "style_score": 0.2784,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "800e79f8-97a2-424c-8af4-35c90e4cb49f",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5702,
  "model_score": 0.6114,
  "style_score": 0.5199,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "c4a335ac-764c-4e50-a6b5-088e64c26351",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2195,
  "model_score": 0.3212,
  "style_score": 0.0952,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "79a68553-bb7c-4314-ba71-fd8dda7f80ab",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.3784,
  "model_score": 0.5727,
  "style_score": 0.1275,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "6b47a5a5-3bc8-4594-844b-5935af16b326",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.6125,
  "model_score": 0.5862,
  "style_score": 0.6447,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "d9cc1aa4-0606-4992-8b00-be2916efbd0f",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.3172,
  "model_score": 0.2452,
  "style_score": 0.4053,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "0a1c87ec-3b17-4fb0-87af-1d2cec8af786",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5049,
  "model_score": 0.7042,
  "style_score": 0.2619,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "0e9b3e2d-198d-438b-9d51-154e130f6c00",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.7625,
  "model_score": 0.9792,
  "style_score": 0.5286,
  "label": "This text looks like it was mostly produced by an AI writing tool rather than written directly by a person.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "366c37c6-94ee-4725-85bd-d5510bd15995",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.4724,
  "model_score": 0.6175,
  "style_score": 0.295,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "a16ea845-ee60-4588-b088-387acc6af8d3",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.6233,
  "model_score": 0.7387,
  "style_score": 0.4822,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "ef4a390f-5a79-4204-a4b1-6fd6b188a3d3",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.6209,
  "model_score": 0.8051,
  "style_score": 0.403,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "fe8c7e78-f504-4fbe-995e-d830879cace3",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6094,
  "model_score": 0.8329,
  "style_score": 0.3532,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "42a7923a-6830-4ff9-b5d4-c2af01b0a499",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.6609,
  "model_score": 0.8005,
  "style_score": 0.4902,
  "label": "This text looks like it was mostly produced by an AI writing tool rather than written directly by a person.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "b98a646f-8ddd-4871-8958-c69c28d5ff77",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5755,
  "model_score": 0.8814,
  "style_score": 0.2313,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "8908723d-58ec-4b0a-b0c0-31a3ff460bdb",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5702,
  "model_score": 0.8816,
  "style_score": 0.2186,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "3318750f-c312-4e82-a4ef-346c46cf731d",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.2599,
  "model_score": 0.3223,
  "style_score": 0.1836,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "02b51b00-1fc2-4108-9b0a-24e0498cb2bf",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.3092,
  "model_score": 0.4625,
  "style_score": 0.1219,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "0493c3c6-60b8-4d9d-ae11-4d6c9278bf5e",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1548,
  "model_score": 0.2044,
  "style_score": 0.0941,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "51a6b856-ba0b-4b4e-9973-b235caf832e5",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.4962,
  "model_score": 0.5943,
  "style_score": 0.3763,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "73a9ae41-7a72-4304-bfd1-42f65ed01404",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.3888,
  "model_score": 0.4998,
  "style_score": 0.2531,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "d3352c33-a7ee-4540-ad78-634bc986345f",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4256,
  "model_score": 0.6401,
  "style_score": 0.1511,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "ffc7f3a3-3964-4eca-b709-c8a31ad75381",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.445,
  "model_score": 0.5583,
  "style_score": 0.3065,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "b1787e64-f9c0-4b83-be65-385c3de221e0",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.2728,
  "model_score": 0.0,
  "style_score": 0.55,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "a4a59c73-7e4c-4b8f-9535-5fd324de0ca7",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.4159,
  "model_score": 0.0112,
  "style_score": 0.85,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "6dcc54e6-0801-4b80-b922-2b117452a186",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8637,
  "model_score": 0.9976,
  "style_score": 0.7,
  "label": "This text looks like it was mostly produced by an AI writing tool rather than written directly by a person.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "c5812706-5ff2-429e-a86d-69a4ad87b8b8",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9308,
  "model_score": 0.9969,
  "style_score": 0.85,
  "label": "This text looks like it was mostly produced by an AI writing tool rather than written directly by a person.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "379e7e7d-baea-495b-9640-c6aed3e29f4a",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9408,
  "model_score": 0.9064,
  "style_score": 0.9829,
  "label": "This text looks like it was mostly produced by an AI writing tool rather than written directly by a person.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "d5a117fa-6810-44ea-98be-871fd4c40359",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.8076,
  "model_score": 0.9876,
  "style_score": 0.6005,
  "label": "This text looks like it was mostly produced by an AI writing tool rather than written directly by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "9e7af23c-cd34-412d-8447-986221d7d976",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3426,
  "model_score": 0.0287,
  "style_score": 0.6673,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "40018f87-8365-4af0-ac80-0d3d3e7a6479",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3426,
  "model_score": 0.0287,
  "style_score": 0.6673,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "b2d11841-bc37-4a6c-a763-1f0605f74625",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3426,
  "model_score": 0.0287,
  "style_score": 0.6673,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "f5e79896-18c5-46a3-a4f8-dd3e8daaf618",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3426,
  "model_score": 0.0287,
  "style_score": 0.6673,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "5d90412b-8065-4731-af64-87a8520a1693",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3426,
  "model_score": 0.0287,
  "style_score": 0.6673,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "b6a6471d-98e2-42e7-bb34-fef08ba08012",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3426,
  "model_score": 0.0287,
  "style_score": 0.6673,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "933eb954-c1a5-40c2-83e4-9cca71d4a100",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3426,
  "model_score": 0.0287,
  "style_score": 0.6673,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "07387b64-2764-44ce-9287-9cc6682ddd3c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3426,
  "model_score": 0.0287,
  "style_score": 0.6673,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "ffbbc999-880e-4871-a205-8bc0e5daf778",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3426,
  "model_score": 0.0287,
  "style_score": 0.6673,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "ccf02e52-d0ce-45bd-85f7-a9bab45fccc4",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3426,
  "model_score": 0.0287,
  "style_score": 0.6673,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
