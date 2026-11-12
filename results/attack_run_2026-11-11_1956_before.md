# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 19:56
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `dd76ff45-616c-4fab-b496-26d5517d6502` | human | 0.332 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `46349b49-6e32-4ef5-8ff0-1fbd5612c089` | unsure | 0.384 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `8b2c2cf9-39d1-40fc-81f5-9dd0245f41d1` | unsure | 0.492 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `65914cda-5ad8-41c3-a915-708793a03fde` | unsure | 0.570 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `7eb7bf67-7df4-4cb7-be71-eda99fba1cf9` | human | 0.220 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `feaa0fdd-4d73-4f0c-9dfa-9de15dcc7e62` | unsure | 0.378 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `08b35eab-db73-4d3a-94a9-aab73f9ac7e9` | unsure | 0.613 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `d5c918d7-ab3f-4efc-ab5b-4a00e96953d8` | human | 0.317 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `28922cdf-352f-42bb-8c38-fad62ab2d030` | unsure | 0.505 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `67619d5f-671c-4693-8b2c-576c2aadef3a` | ai | 0.762 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `d74eb324-644a-4a67-8fa7-aef6de4f39c5` | unsure | 0.472 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `2491fd2a-a29c-4d32-9ae0-866176cdd716` | unsure | 0.623 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `b346a076-57f2-43b9-bf9f-7f042f88f0a4` | unsure | 0.621 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `f57973a0-2f45-4645-92a1-9d203cdebc0c` | unsure | 0.609 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `e3b2bc80-2bfc-4a9c-b684-68189833b00d` | ai | 0.661 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `cffd0abe-46c6-4777-b6a4-04d43d7d585c` | unsure | 0.576 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `e33df08e-278f-4da6-bc25-f2ba967a7192` | unsure | 0.570 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `86d6f639-4578-4fa7-a224-86ce876b1668` | human | 0.260 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `0a3e0762-419c-42fa-8f1f-cee05c95ed14` | human | 0.309 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `4134e612-0476-40b7-a4d8-ceeec01f0416` | human | 0.155 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `fd40e443-7a3b-43ad-ae5e-7c2875084d62` | unsure | 0.496 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `e8b5f6a3-864a-4b12-b8ba-87ee9a2d3dd1` | unsure | 0.389 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `fec2d238-ed21-4537-a01f-9c9edcd72542` | unsure | 0.426 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c6527d9f-163a-4787-b9c5-6ecbb68e41c0` | unsure | 0.445 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `866fabf6-838b-4490-bc03-83188d40b89e` | human | 0.273 |  |
| MF04 | malformed | text is only punctuation | 200 | `cffe08d1-5e5d-4d00-ab8d-d311e417cc10` | unsure | 0.416 |  |
| MF05 | malformed | text is a very long single word | 200 | `97fb358c-9a9a-4522-b81d-dbf83adc39de` | ai | 0.864 |  |
| MF06 | malformed | text is emoji only | 200 | `221fb027-3768-4ca8-805e-01907c2f4b7e` | ai | 0.931 |  |
| MF07 | malformed | text is right-to-left script | 200 | `66743c31-9ea0-4266-aa4a-dcd6772e0b4e` | ai | 0.941 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `f43eee1b-099c-4acf-9890-8e45f1ec5d2a` | ai | 0.808 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `12e59f77-c604-49ee-a9fc-14ed49b9e0cd` | human | 0.343 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d83d8f36-2c3e-4a57-bcd4-a0c8670c8ab1` | human | 0.343 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e8727dbc-aa47-44b6-bbcb-a4ce0e90d211` | human | 0.343 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e5f702ba-813f-46b0-a692-7eeffebf2fe5` | human | 0.343 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0b0b974b-9f0a-4f5b-a363-6f38c38d54ba` | human | 0.343 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5dc21972-45c4-4e53-97e8-95973f38e4b3` | human | 0.343 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c46d6d57-ab0b-44d6-8da1-3628e012c094` | human | 0.343 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `231cb7b5-a665-46a6-9ffb-06c67ab87870` | human | 0.343 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `26d62f79-791e-4073-94d4-51d8c3e8e1e5` | human | 0.343 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ef55f77f-ea81-42a7-881e-be2052b81268` | human | 0.343 |  |
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
  "content_id": "dd76ff45-616c-4fab-b496-26d5517d6502",
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
  "content_id": "46349b49-6e32-4ef5-8ff0-1fbd5612c089",
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
  "content_id": "8b2c2cf9-39d1-40fc-81f5-9dd0245f41d1",
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
  "content_id": "65914cda-5ad8-41c3-a915-708793a03fde",
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
  "content_id": "7eb7bf67-7df4-4cb7-be71-eda99fba1cf9",
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
  "content_id": "feaa0fdd-4d73-4f0c-9dfa-9de15dcc7e62",
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
  "content_id": "08b35eab-db73-4d3a-94a9-aab73f9ac7e9",
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
  "content_id": "d5c918d7-ab3f-4efc-ab5b-4a00e96953d8",
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
  "content_id": "28922cdf-352f-42bb-8c38-fad62ab2d030",
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
  "content_id": "67619d5f-671c-4693-8b2c-576c2aadef3a",
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
  "content_id": "d74eb324-644a-4a67-8fa7-aef6de4f39c5",
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
  "content_id": "2491fd2a-a29c-4d32-9ae0-866176cdd716",
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
  "content_id": "b346a076-57f2-43b9-bf9f-7f042f88f0a4",
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
  "content_id": "f57973a0-2f45-4645-92a1-9d203cdebc0c",
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
  "content_id": "e3b2bc80-2bfc-4a9c-b684-68189833b00d",
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
  "content_id": "cffd0abe-46c6-4777-b6a4-04d43d7d585c",
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
  "content_id": "e33df08e-278f-4da6-bc25-f2ba967a7192",
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
  "content_id": "86d6f639-4578-4fa7-a224-86ce876b1668",
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
  "content_id": "0a3e0762-419c-42fa-8f1f-cee05c95ed14",
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
  "content_id": "4134e612-0476-40b7-a4d8-ceeec01f0416",
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
  "content_id": "fd40e443-7a3b-43ad-ae5e-7c2875084d62",
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
  "content_id": "e8b5f6a3-864a-4b12-b8ba-87ee9a2d3dd1",
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
  "content_id": "fec2d238-ed21-4537-a01f-9c9edcd72542",
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
  "content_id": "c6527d9f-163a-4787-b9c5-6ecbb68e41c0",
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
  "content_id": "866fabf6-838b-4490-bc03-83188d40b89e",
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
  "content_id": "cffe08d1-5e5d-4d00-ab8d-d311e417cc10",
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
  "content_id": "97fb358c-9a9a-4522-b81d-dbf83adc39de",
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
  "content_id": "221fb027-3768-4ca8-805e-01907c2f4b7e",
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
  "content_id": "66743c31-9ea0-4266-aa4a-dcd6772e0b4e",
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
  "content_id": "f43eee1b-099c-4acf-9890-8e45f1ec5d2a",
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
  "content_id": "12e59f77-c604-49ee-a9fc-14ed49b9e0cd",
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
  "content_id": "d83d8f36-2c3e-4a57-bcd4-a0c8670c8ab1",
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
  "content_id": "e8727dbc-aa47-44b6-bbcb-a4ce0e90d211",
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
  "content_id": "e5f702ba-813f-46b0-a692-7eeffebf2fe5",
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
  "content_id": "0b0b974b-9f0a-4f5b-a363-6f38c38d54ba",
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
  "content_id": "5dc21972-45c4-4e53-97e8-95973f38e4b3",
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
  "content_id": "c46d6d57-ab0b-44d6-8da1-3628e012c094",
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
  "content_id": "231cb7b5-a665-46a6-9ffb-06c67ab87870",
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
  "content_id": "26d62f79-791e-4073-94d4-51d8c3e8e1e5",
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
  "content_id": "ef55f77f-ea81-42a7-881e-be2052b81268",
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
