"""
Hand-checked cases for scoring.combine_signals.

The README sample (model 0.45 / style 0.14) has a gap of 0.31, which is
*below* DISAGREEMENT_GAP 0.35, so it never pulled toward 0.5. These two
inputs sit on either side of that cutoff.

    python test_combine.py
"""

import config
import scoring


def _mix(model_score: float, style_score: float) -> float:
    return (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
    )


def test_below_cutoff_does_not_pull():
    """gap 0.34 → weighted mix only, no pull toward 0.5."""
    model, style = 0.80, 0.46
    assert round(abs(model - style), 2) == 0.34
    assert round(abs(model - style), 2) <= config.DISAGREEMENT_GAP
    expected = round(_mix(model, style), 4)  # 0.55*0.80 + 0.30*0.46 = 0.5780
    assert expected == 0.5780
    got = scoring.combine_signals(model, style)
    assert got == expected, f"below cutoff: expected {expected}, got {got}"


def test_above_cutoff_pulls_toward_half():
    """gap 0.70 → mix 0.5550, then pull 0.175 of the way toward 0.5 → 0.5454."""
    model, style = 0.90, 0.20
    gap = abs(model - style)
    assert round(gap, 2) == 0.70
    assert gap > config.DISAGREEMENT_GAP
    unpulled = _mix(model, style)  # 0.55*0.90 + 0.30*0.20 = 0.555
    pull = min(
        (gap - config.DISAGREEMENT_GAP) / config.DISAGREEMENT_RAMP,
        1.0,
    ) * config.DISAGREEMENT_PULL  # (0.35 / 0.5) * 0.25 = 0.175
    expected = round(unpulled * (1.0 - pull) + 0.5 * pull, 4)
    assert expected == 0.5454
    got = scoring.combine_signals(model, style)
    assert got == expected, f"above cutoff: expected {expected}, got {got}"
    assert got != round(unpulled, 4), "pull toward 0.5 should have moved the mix"


def test_readme_sample_does_not_trigger_disagreement():
    """The live sample (0.4511 / 0.1391) is a split, but the gap is 0.312."""
    model, style = 0.4511, 0.1391
    assert abs(model - style) < config.DISAGREEMENT_GAP
    got = scoring.combine_signals(model, style)
    assert got == round(_mix(model, style), 4)


if __name__ == "__main__":
    test_below_cutoff_does_not_pull()
    test_above_cutoff_pulls_toward_half()
    test_readme_sample_does_not_trigger_disagreement()
    print("combine_signals: three hand-checked cases passed")
