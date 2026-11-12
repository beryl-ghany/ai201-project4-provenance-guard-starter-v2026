# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 20:03
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `98e64a45-3d08-4f8f-be54-f469fb59b5b7` | human | 0.332 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `cb735ad1-65bc-4138-a9da-9b41d653dbee` | unsure | 0.384 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `5f43373e-3c22-401b-8b7e-8b308942e7fe` | unsure | 0.492 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `7827220d-7e19-4be0-bbfd-6c144fe2f611` | unsure | 0.570 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `ae859382-06a2-4f6a-ba2d-dbb2298ab4e0` | human | 0.220 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `2c1dd5b6-c052-4098-a5f7-7ea6a1a8a256` | unsure | 0.378 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `947fecaa-c715-4b43-a95a-4077159754da` | unsure | 0.613 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `83ff26ac-9e7a-4489-a094-8262484b8761` | human | 0.317 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `de64c6ac-9397-4ec1-ad25-95746d8818ff` | unsure | 0.505 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `b474f904-56e7-4ab9-964c-d87d9d6d1aae` | ai | 0.762 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `cb85088b-ef00-4e19-a68f-6034f43038fc` | unsure | 0.472 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `7e1ebe67-c4ac-4076-9a12-3f91b920124d` | unsure | 0.623 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `1b0c0f1f-c827-46e2-8af4-dcda2ef0a0ed` | unsure | 0.621 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `bb21e5aa-9e90-4299-9e4d-4ef1211f4612` | unsure | 0.609 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `89eba045-9589-457d-995d-b2be900de208` | ai | 0.661 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `c2c8c3d6-72eb-471d-a426-63cfc57c1b45` | unsure | 0.576 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `863acbc7-8609-44b5-87d5-cb7db7ceecf4` | unsure | 0.570 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `2256d880-9ba8-4dde-b8bb-63b3bc2775b7` | human | 0.260 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `374bcc48-07b2-45ea-abdf-c7d672a2c988` | human | 0.309 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `82a1c445-e7e4-4856-ac89-d966bf0bb948` | human | 0.155 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `aafb54bc-8ccf-4b4d-ae50-f9a70ec78e5d` | unsure | 0.496 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `f73737ea-ec43-4c4f-8ed8-967cc254eb82` | unsure | 0.389 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `f97d9339-b4a5-4282-acce-449648d5700e` | unsure | 0.426 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `2c72e640-627e-49b2-a8cc-56921628226c` | unsure | 0.445 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `14cb47cb-1375-4378-a470-fe4bbb2d92ca` | human | 0.273 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `e0ed834e-a73b-4ba6-a78b-b51a40acb318` | unsure | 0.416 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `5a546871-44b6-46d6-b6fd-da2a129b6751` | ai | 0.864 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `b51cf6e1-a4da-4e29-99a9-ca4301778824` | ai | 0.931 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `18651ded-1c83-457c-b8bb-7f870383ff1c` | ai | 0.941 | BROKE |
| MF08 | malformed | text is 60,000 characters | 200 | `57da242d-d2d5-4db7-b6b4-fe59e5730ed2` | ai | 0.808 | BROKE |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e4395fe2-6d4a-4832-ac42-746f69c5770c` | human | 0.343 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `27d8a2e5-7e60-4ac6-8fad-ab03d688401a` | human | 0.343 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a63dfbf7-92fa-41db-ac73-197bf0be3057` | human | 0.343 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `af8d54f4-fa62-4f8e-a8a2-3f0ff842139d` | human | 0.343 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f7e71bd2-61dc-4441-bcc1-4f4afe9f148b` | human | 0.343 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9e95443f-95c9-4d94-b177-05af5270ce04` | human | 0.343 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b838ef0d-0158-4bcc-b3e1-e8100e97a040` | human | 0.343 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `af0adc8a-c8c3-43b8-85b9-bd98867e4ac7` | human | 0.343 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1f71e82d-119d-49af-8a29-c0d7842f6d88` | human | 0.343 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b05880a3-7b9f-4dd7-ba53-f8e893126089` | human | 0.343 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

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
  "content_id": "98e64a45-3d08-4f8f-be54-f469fb59b5b7",
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
  "content_id": "cb735ad1-65bc-4138-a9da-9b41d653dbee",
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
  "content_id": "5f43373e-3c22-401b-8b7e-8b308942e7fe",
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
  "content_id": "7827220d-7e19-4be0-bbfd-6c144fe2f611",
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
  "content_id": "ae859382-06a2-4f6a-ba2d-dbb2298ab4e0",
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
  "content_id": "2c1dd5b6-c052-4098-a5f7-7ea6a1a8a256",
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
  "content_id": "947fecaa-c715-4b43-a95a-4077159754da",
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
  "content_id": "83ff26ac-9e7a-4489-a094-8262484b8761",
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
  "content_id": "de64c6ac-9397-4ec1-ad25-95746d8818ff",
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
  "content_id": "b474f904-56e7-4ab9-964c-d87d9d6d1aae",
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
  "content_id": "cb85088b-ef00-4e19-a68f-6034f43038fc",
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
  "content_id": "7e1ebe67-c4ac-4076-9a12-3f91b920124d",
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
  "content_id": "1b0c0f1f-c827-46e2-8af4-dcda2ef0a0ed",
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
  "content_id": "bb21e5aa-9e90-4299-9e4d-4ef1211f4612",
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
  "content_id": "89eba045-9589-457d-995d-b2be900de208",
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
  "content_id": "c2c8c3d6-72eb-471d-a426-63cfc57c1b45",
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
  "content_id": "863acbc7-8609-44b5-87d5-cb7db7ceecf4",
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
  "content_id": "2256d880-9ba8-4dde-b8bb-63b3bc2775b7",
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
  "content_id": "374bcc48-07b2-45ea-abdf-c7d672a2c988",
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
  "content_id": "82a1c445-e7e4-4856-ac89-d966bf0bb948",
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
  "content_id": "aafb54bc-8ccf-4b4d-ae50-f9a70ec78e5d",
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
  "content_id": "f73737ea-ec43-4c4f-8ed8-967cc254eb82",
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
  "content_id": "f97d9339-b4a5-4282-acce-449648d5700e",
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
  "content_id": "2c72e640-627e-49b2-a8cc-56921628226c",
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
  "content_id": "14cb47cb-1375-4378-a470-fe4bbb2d92ca",
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
  "content_id": "e0ed834e-a73b-4ba6-a78b-b51a40acb318",
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
  "content_id": "5a546871-44b6-46d6-b6fd-da2a129b6751",
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
  "content_id": "b51cf6e1-a4da-4e29-99a9-ca4301778824",
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
  "content_id": "18651ded-1c83-457c-b8bb-7f870383ff1c",
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
  "content_id": "57da242d-d2d5-4db7-b6b4-fe59e5730ed2",
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
  "content_id": "e4395fe2-6d4a-4832-ac42-746f69c5770c",
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
  "content_id": "27d8a2e5-7e60-4ac6-8fad-ab03d688401a",
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
  "content_id": "a63dfbf7-92fa-41db-ac73-197bf0be3057",
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
  "content_id": "af8d54f4-fa62-4f8e-a8a2-3f0ff842139d",
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
  "content_id": "f7e71bd2-61dc-4441-bcc1-4f4afe9f148b",
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
  "content_id": "9e95443f-95c9-4d94-b177-05af5270ce04",
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
  "content_id": "b838ef0d-0158-4bcc-b3e1-e8100e97a040",
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
  "content_id": "af0adc8a-c8c3-43b8-85b9-bd98867e4ac7",
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
  "content_id": "1f71e82d-119d-49af-8a29-c0d7842f6d88",
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
  "content_id": "b05880a3-7b9f-4dd7-ba53-f8e893126089",
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