# Attack run — after2

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 20:09
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `b9513b92-e0aa-4d97-ae31-a32f074ebe84` | human | 0.253 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `b6f2bc82-d755-459c-af2f-1451407dca72` | unsure | 0.369 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `95deae2a-fc2c-420d-8a38-f81022172902` | unsure | 0.451 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `e7fa2138-a832-45c1-bbbc-47e6dfcca564` | unsure | 0.492 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `abb6e768-5546-4b10-b632-f2445521c57b` | human | 0.205 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `7c8be77a-5d82-4621-b6ff-63e08d3b85b8` | unsure | 0.360 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `81628829-4c13-4b60-a0c9-ef688f8f19c5` | unsure | 0.516 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `fb68a15a-7868-477d-8426-a0d85164c846` | human | 0.257 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `15627567-c8d3-4383-b05f-cd8a2a4a5b5b` | unsure | 0.468 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `de231293-b4d5-41d7-88e0-95d4a6f15e38` | ai | 0.687 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `a6b5cf0d-8c37-4ae0-b7bb-708f8d2958a0` | unsure | 0.428 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `4d886769-2e5d-451b-b411-2a5b8de7d4b2` | unsure | 0.551 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `842a38e9-9120-4321-bbf2-99a282a45fa0` | unsure | 0.562 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `566fb750-c238-4e29-be69-da8e146510ef` | unsure | 0.560 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `7d2e4a40-351b-48bf-b0f0-e1783315a143` | unsure | 0.587 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `cde4fc57-83ca-4fa0-88e8-5dde608c1feb` | unsure | 0.546 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `535c3e62-6989-4e14-8a52-486a9fd8d197` | unsure | 0.543 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `84e769c3-40ad-487a-81ac-58b30f1ce30c` | human | 0.232 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `8186e55c-47ab-477d-9ea1-ed1b908041e4` | human | 0.291 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `e8a18e58-0441-44e5-a0e4-b54afb3fb7c1` | human | 0.141 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `241d04e1-9c36-470c-98f0-d5090e3ffebd` | unsure | 0.440 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `6c6796ab-2b93-4f27-9014-d15ea6891f8d` | unsure | 0.351 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `573febf1-6bc1-4b18-ba6f-0ba7fe2b9ecd` | unsure | 0.405 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `9bc7ef78-ffd6-4b23-8553-f9e99890e1b5` | unsure | 0.399 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `e701ebae-c8fb-4a04-9b1e-b71b89252698` | human | 0.199 |  |
| MF04 | malformed | text is only punctuation | 200 | `796a9e85-8afc-426a-be3f-69665a11a44c` | human | 0.320 |  |
| MF05 | malformed | text is a very long single word | 200 | `2b64474e-65c8-4106-8d77-2d912d38cdd4` | ai | 0.759 |  |
| MF06 | malformed | text is emoji only | 200 | `c7410c73-a58c-46b3-8bc0-bb46bc038320` | ai | 0.803 |  |
| MF07 | malformed | text is right-to-left script | 200 | `30bc1275-9469-490b-b89a-629de73f84de` | ai | 0.793 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `8c18f513-aca5-4c52-9cf7-a43cbc737900` | ai | 0.719 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e0cfb894-2ea5-43a5-be78-1b7923d97d21` | human | 0.257 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8d000899-c2d8-4f41-b49c-fcc7ea4422ec` | human | 0.257 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7d3f0b43-9627-43a4-8877-d57707ceacbc` | human | 0.257 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `85889940-6b48-48e0-95da-0525834d1ada` | human | 0.257 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `32a0f74a-47bf-4362-bf82-baaefddffe2e` | human | 0.257 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5d4fe258-c6e9-4d77-9495-2563846d8855` | human | 0.257 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `30c9452d-5a33-456f-9d83-de5630c315cb` | human | 0.257 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `eca78dab-166f-49f4-b056-9de03263de8f` | human | 0.257 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e2a6f240-6db1-433c-921c-66bb338dcbc7` | human | 0.257 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cfd63159-3ffe-46ef-9754-bb2e1d1c95ca` | human | 0.257 |  |
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
  "content_id": "b9513b92-e0aa-4d97-ae31-a32f074ebe84",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.2526,
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
  "content_id": "b6f2bc82-d755-459c-af2f-1451407dca72",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.3686,
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
  "content_id": "95deae2a-fc2c-420d-8a38-f81022172902",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.4509,
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
  "content_id": "e7fa2138-a832-45c1-bbbc-47e6dfcca564",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.4922,
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
  "content_id": "abb6e768-5546-4b10-b632-f2445521c57b",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2052,
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
  "content_id": "7c8be77a-5d82-4621-b6ff-63e08d3b85b8",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.3602,
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
  "content_id": "81628829-4c13-4b60-a0c9-ef688f8f19c5",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5158,
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
  "content_id": "fb68a15a-7868-477d-8426-a0d85164c846",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.2565,
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
  "content_id": "15627567-c8d3-4383-b05f-cd8a2a4a5b5b",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.4675,
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
  "content_id": "de231293-b4d5-41d7-88e0-95d4a6f15e38",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.6872,
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
  "content_id": "a6b5cf0d-8c37-4ae0-b7bb-708f8d2958a0",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.4281,
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
  "content_id": "4d886769-2e5d-451b-b411-2a5b8de7d4b2",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.5509,
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
  "content_id": "842a38e9-9120-4321-bbf2-99a282a45fa0",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.562,
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
  "content_id": "566fb750-c238-4e29-be69-da8e146510ef",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.5599,
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
  "content_id": "7d2e4a40-351b-48bf-b0f0-e1783315a143",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.5873,
  "model_score": 0.8005,
  "style_score": 0.4902,
  "label": "We are not sure whether a person or a writing tool produced this. You can ask for a human review if you think we got it wrong.",
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
  "content_id": "cde4fc57-83ca-4fa0-88e8-5dde608c1feb",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.546,
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
  "content_id": "535c3e62-6989-4e14-8a52-486a9fd8d197",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5426,
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
  "content_id": "84e769c3-40ad-487a-81ac-58b30f1ce30c",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.2323,
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
  "content_id": "8186e55c-47ab-477d-9ea1-ed1b908041e4",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.2909,
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
  "content_id": "e8a18e58-0441-44e5-a0e4-b54afb3fb7c1",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1406,
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
  "content_id": "241d04e1-9c36-470c-98f0-d5090e3ffebd",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.4398,
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
  "content_id": "6c6796ab-2b93-4f27-9014-d15ea6891f8d",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.3508,
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
  "content_id": "573febf1-6bc1-4b18-ba6f-0ba7fe2b9ecd",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4045,
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
  "content_id": "9bc7ef78-ffd6-4b23-8553-f9e99890e1b5",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.399,
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
  "content_id": "e701ebae-c8fb-4a04-9b1e-b71b89252698",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.1985,
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
  "content_id": "796a9e85-8afc-426a-be3f-69665a11a44c",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.3195,
  "model_score": 0.0112,
  "style_score": 0.85,
  "label": "This looks like it was written by a person. We are not treating it as AI-generated.",
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
  "content_id": "2b64474e-65c8-4106-8d77-2d912d38cdd4",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7587,
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
  "content_id": "c7410c73-a58c-46b3-8bc0-bb46bc038320",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.8033,
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
  "content_id": "30bc1275-9469-490b-b89a-629de73f84de",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7934,
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
  "content_id": "8c18f513-aca5-4c52-9cf7-a43cbc737900",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.7192,
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
  "content_id": "e0cfb894-2ea5-43a5-be78-1b7923d97d21",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.257,
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
  "content_id": "8d000899-c2d8-4f41-b49c-fcc7ea4422ec",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.257,
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
  "content_id": "7d3f0b43-9627-43a4-8877-d57707ceacbc",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.257,
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
  "content_id": "85889940-6b48-48e0-95da-0525834d1ada",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.257,
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
  "content_id": "32a0f74a-47bf-4362-bf82-baaefddffe2e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.257,
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
  "content_id": "5d4fe258-c6e9-4d77-9495-2563846d8855",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.257,
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
  "content_id": "30c9452d-5a33-456f-9d83-de5630c315cb",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.257,
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
  "content_id": "eca78dab-166f-49f4-b056-9de03263de8f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.257,
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
  "content_id": "e2a6f240-6db1-433c-921c-66bb338dcbc7",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.257,
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
  "content_id": "cfd63159-3ffe-46ef-9754-bb2e1d1c95ca",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.257,
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
