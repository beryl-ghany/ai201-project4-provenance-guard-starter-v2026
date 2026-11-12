"""
What your test runs. ← UNIT 8, MILESTONE 3
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": [
            "I stayed up until two finishing this draft. My sentences are all over the place — "
            "some tiny, some way too long — and I keep changing my mind mid-paragraph about "
            "whether the ending works. Nobody asked me to write it; I just needed to get it out.",
            "The bus was late again so I walked. Cold air, wet sneakers, my phone at twelve percent. "
            "I thought about calling home and did not. Sometimes silence is easier than explaining.",
            "My lab partner and I argued about error bars for twenty minutes. I still think we "
            "should have used the wider interval, but the graph looked fine and we handed it in anyway.",
            "Sunday laundry, then curry rice for dinner. I forgot the cilantro. It tasted fine without it, "
            "which annoyed me more than it should have.",
            "Dear future me: stop buying notebooks you never open. This one is different. (It is not.)",
            "I rewrote the opening sentence six times. The sixth version is worse. I kept it because "
            "starting over again felt impossible tonight.",
            "Rain on the window during office hours. Three students canceled. I graded anyway and "
            "left comments that were probably too long.",
            "He said he was proud of me and I did not know what to say, so I nodded and changed the subject.",
            "The playlist shuffle picked the wrong song at the wrong moment. I turned it off and "
            "listened to traffic instead.",
            "I am tired of pretending I have a five-year plan. I have next week and a list on my fridge.",
        ],
    },
    {
        "name": "calibration spread",
        "criterion": 2,
        "texts": [
            "The implementation of the proposed framework requires careful consideration of several "
            "key factors. First, it is important to note that the system must be able to handle a wide "
            "variety of different inputs. Additionally, the overall performance of the solution depends "
            "on a number of important variables.",
            "I stayed up until two finishing this draft. My sentences are all over the place — some tiny, "
            "some way too long — and I keep changing my mind mid-paragraph about whether the ending works.",
            "I go store. Buy milk. Walk home. Rain. Shoes wet. Phone die. No call mom.",
            "The implementation of the proposed framework requires careful consideration of several key factors. "
            "Honestly though? I rewrote this twice and my cat walked on the keyboard once, so maybe that "
            "counts as human editing.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            "In conclusion, it is worth noting that the aforementioned considerations demonstrate the "
            "importance of a comprehensive approach. Furthermore, stakeholders should prioritize "
            "scalability, maintainability, and robustness when evaluating potential solutions. "
            "This ensures long-term viability and alignment with organizational objectives.",
            "I spilled coffee on my hoodie, laughed at myself, and took the long way to class because "
            "the shortcut smells like dumpsters in November and I was already in a mood.",
            "The results are mixed. Some of it reads smooth and some of it sounds like me on a bad "
            "Tuesday—half proud, half unsure, and too tired to fight about commas.",
        ],
    },
    {
        "name": "appeal path",
        "criterion": 4,
        # Submit each text, then POST /appeal with the content_id that came back.
        # Pass = HTTP 200 on the appeal AND a log row with event=appeal / under_review.
        "then_appeal": True,
        "texts": [
            "Appeal test one: I wrote this on the train, half distracted, all mine.",
            "Appeal test two: my sister proofread typos only; the ideas are still mine.",
            "Appeal test three: short note to myself about groceries and overdue emails.",
            "Appeal test four: rant about parking tickets. Petty, human, unfortunately accurate.",
            "Appeal test five: draft email I never sent to my professor about extensions.",
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        # Pass = HTTP 400 and no new audit row with a guess field.
        "expect_status": 400,
        "expect_no_guess": True,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   ", "creator_id": "eval_bad_whitespace"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"creator_id": "eval_bad_missing_text"},
            {"text": "tiny", "creator_id": "eval_bad_short"},
        ],
    },
]


def trial_summary(scenario: dict, results: list[dict]) -> str:
    """One-cell summary for the Run Log table. Criteria 4 and 5 are auto-checked."""
    criterion = scenario.get("criterion")
    if criterion == 4:
        n = sum(1 for r in results if r.get("appeal_ok") and r.get("log_under_review"))
        return f"{n}/{len(results)} appeal + log"
    if criterion == 5:
        n = sum(
            1 for r in results
            if r.get("status") == scenario.get("expect_status", 400)
            and not r.get("guess")
            and not r.get("guess_row_in_log")
        )
        return f"{n}/{len(results)} return 400, no guess row"
    guesses = [r.get("guess") or "—" for r in results]
    return ", ".join(guesses)


def trial_passed(scenario: dict, results: list[dict]) -> bool | None:
    """True/False for criteria 4 and 5; None when the verdict is a judgment call."""
    criterion = scenario.get("criterion")
    if criterion == 4:
        return all(r.get("appeal_ok") and r.get("log_under_review") for r in results)
    if criterion == 5:
        want = scenario.get("expect_status", 400)
        return all(
            r.get("status") == want
            and not r.get("guess")
            and not r.get("guess_row_in_log")
            for r in results
        )
    return None


def validate() -> list[str]:
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
