"""Ratio gate only. Does not load the model."""

import capstone_cases
import writing_check

ARABIC = "هذا نص باللغة العربية لاختبار كيفية تعامل النظام مع النصوص المكتوبة."


def test_non_writing_is_below_the_ratio():
    assert len(capstone_cases.NOT_WRITING) == 5
    for text in capstone_cases.NOT_WRITING:
        assert len(text.strip()) >= 20, text
        assert writing_check.letter_ratio(text) < 0.40, (text, writing_check.letter_ratio(text))
        assert not writing_check.is_writing(text)


def test_prose_clears_the_ratio():
    assert len(capstone_cases.WRITING) == 5
    for text in capstone_cases.WRITING:
        assert len(text.strip()) >= 20
        assert writing_check.letter_ratio(text) >= 0.60, (writing_check.letter_ratio(text), text)
        assert writing_check.is_writing(text)
    assert writing_check.letter_ratio(capstone_cases.LATENCY_TEXT) >= 0.60


def test_arabic_letters_count_as_writing():
    assert writing_check.is_writing(ARABIC)


def test_repeated_letter_is_not_writing():
    """Ratio is 1.0. One distinct letter is still not a piece of writing."""
    assert writing_check.letter_ratio(capstone_cases.REPEATED_LETTER) == 1.0
    assert writing_check.distinct_letters(capstone_cases.REPEATED_LETTER) == 1
    assert not writing_check.is_writing(capstone_cases.REPEATED_LETTER)


if __name__ == "__main__":
    test_non_writing_is_below_the_ratio()
    test_prose_clears_the_ratio()
    test_arabic_letters_count_as_writing()
    test_repeated_letter_is_not_writing()
    print("writing_check ok")
