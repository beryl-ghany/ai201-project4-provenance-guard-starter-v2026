"""
Refuse text that is long enough to score and still not writing.

Unit 8 let punctuation, emoji, and digit strings through the length check.
Both signals then invented a guess. This gate runs first: if Unicode letters
are too small a share of the string, the route rejects it and the model
never loads that body.

The ratio is letters / len(text), spaces included, on the string that would
otherwise be scored (after the length cap, before either signal).
"""

import config


def letter_ratio(text: str) -> float:
    """Share of characters that are Unicode letters. Empty text is 0."""
    if not text:
        return 0.0
    letters = sum(1 for ch in text if ch.isalpha())
    return letters / len(text)


def is_writing(text: str) -> bool:
    """True when the string clears MIN_LETTER_RATIO."""
    return letter_ratio(text) >= config.MIN_LETTER_RATIO
