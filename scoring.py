"""
Turning two numbers into one, and one number into something a person can read.
"""

import config

LABEL_HUMAN = (
    "This looks like it was written by a person. We are not treating it as AI-generated."
)
LABEL_UNSURE = (
    "We are not sure whether a person or a writing tool produced this. "
    "You can ask for a human review if you think we got it wrong."
)
LABEL_AI = (
    "This text looks like it was mostly produced by an AI writing tool rather than "
    "written directly by a person."
)


def combine_signals(model_score: float, style_score: float) -> float:
    """
    Weighted average, pulled toward 0.5 when the two signals disagree —
    disagreement is treated as uncertainty rather than a confident middle guess.
    """
    base = (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
    )
    gap = abs(model_score - style_score)
    if gap > config.DISAGREEMENT_GAP:
        pull = min(
            (gap - config.DISAGREEMENT_GAP) / config.DISAGREEMENT_RAMP,
            1.0,
        ) * config.DISAGREEMENT_PULL
        base = base * (1.0 - pull) + 0.5 * pull
    return round(min(max(base, 0.0), 1.0), 4)


def score_to_label(score: float) -> tuple[str, str]:
    if score >= config.AI_THRESHOLD:
        return "ai", LABEL_AI
    if score <= config.HUMAN_THRESHOLD:
        return "human", LABEL_HUMAN
    return "unsure", LABEL_UNSURE


def label_ranges() -> list[tuple[str, str]]:
    return [
        ("high-confidence human", f"0.00 – {config.HUMAN_THRESHOLD:.2f}"),
        ("unsure", f"{config.HUMAN_THRESHOLD:.2f} – {config.AI_THRESHOLD:.2f}"),
        ("high-confidence AI", f"{config.AI_THRESHOLD:.2f} – 1.00"),
    ]


if __name__ == "__main__":
    # Hand-checked cases on each side of DISAGREEMENT_GAP. See test_combine.py.
    below = combine_signals(0.80, 0.46)
    above = combine_signals(0.90, 0.20)
    print(f"below cutoff (0.80 vs 0.46, gap 0.34): {below}")
    print(f"above cutoff (0.90 vs 0.20, gap 0.70): {above}")
