"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4
"""

import re
import statistics

import config


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


def sentence_length_spread(text: str) -> float:
    """Coefficient of variation of sentence lengths (words per sentence)."""
    sents = sentences(text)
    if len(sents) < 2:
        return 0.0
    lengths = [len(words(s)) for s in sents]
    mean_len = statistics.mean(lengths)
    if mean_len <= 0:
        return 0.0
    return statistics.stdev(lengths) / mean_len


def type_token_ratio(text: str) -> float:
    """Unique words over total words."""
    w = words(text)
    if not w:
        return 0.0
    return len(set(w)) / len(w)


def punctuation_density(text: str) -> float:
    """Non-word, non-space characters per character of text."""
    if not text.strip():
        return 0.0
    punct = re.findall(r"[^\w\s]", text)
    return len(punct) / len(text)


def _clamp01(value: float) -> float:
    return min(max(value, 0.0), 1.0)


def style_signal(text: str) -> float:
    """
    Higher means more likely AI. Even, repetitive, lightly punctuated prose
    scores higher; lumpy human rhythm scores lower.
    """
    spread = sentence_length_spread(text)
    ttr = type_token_ratio(text)
    punct = punctuation_density(text)

    # Low length spread -> more AI-like (even sentences).
    spread_ai = 1.0 - _clamp01(spread / config.STYLE_SPREAD_NORM)
    # Very high repetition (low TTR on longer text) -> more AI-like.
    ttr_ai = 1.0 - _clamp01(ttr / config.STYLE_TTR_NORM)
    # Sparse punctuation -> slightly more AI-like.
    punct_ai = 1.0 - _clamp01(punct * config.STYLE_PUNCT_SCALE)

    combined = 0.55 * spread_ai + 0.30 * ttr_ai + 0.15 * punct_ai
    return round(_clamp01(combined), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text):.4f}")
    print(f"type_token_ratio         {type_token_ratio(text):.4f}")
    print(f"punctuation_density      {punctuation_density(text):.4f}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
