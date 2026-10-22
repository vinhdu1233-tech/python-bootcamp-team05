import pytest

from members.lnmthi.w1.grades import summary
from members.lnmthi.w1.rules import can_register_thesis, missing
from members.lnmthi.w1.text_tools import top_k, word_count
from members.lnmthi.w1.timetable import by_day
from members.lnmthi.w1.translate import is_palindrome


# Tests for grades.py
def test_summary_basic():
    result = summary([7.5, 9, 6, 8])

    assert result == {
        "min": 6,
        "max": 9,
        "mean": 7.62,
        "median": 7.75,
    }


def test_summary_single_score():
    assert summary([8.5]) == {
        "min": 8.5,
        "max": 8.5,
        "mean": 8.5,
        "median": 8.5,
    }


def test_summary_empty_scores():
    with pytest.raises(ValueError):
        summary([])


# Tests for rules.py
def test_can_register_thesis_eligible():
    assert can_register_thesis(120, 2.0) is True


def test_can_register_thesis_insufficient_credits():
    assert can_register_thesis(119, 3.0) is False


def test_can_register_thesis_low_gpa():
    assert can_register_thesis(130, 1.9) is False


def test_missing_both_requirements():
    assert missing(118, 1.5) == [
        "need 2 more credits",
        "need GPA of 0.50 more",
    ]


def test_missing_no_requirements():
    assert missing(120, 2.0) == []


# Tests for text_tools.py
def test_word_count_basic():
    assert word_count("Git is fun. Git is fast!") == {
        "git": 2,
        "is": 2,
        "fun": 1,
        "fast": 1,
    }


def test_word_count_case_and_punctuation():
    assert word_count("Hello, HELLO! World.") == {
        "hello": 2,
        "world": 1,
    }


def test_word_count_empty_text():
    assert word_count("") == {}


def test_top_k_ordering():
    assert top_k("b a b c a b", 2) == [
        ("b", 3),
        ("a", 2),
    ]


def test_top_k_ties_alphabetically():
    assert top_k("banana apple", 2) == [
        ("apple", 1),
        ("banana", 1),
    ]


def test_top_k_nonpositive_k():
    assert top_k("a b a", 0) == []
    assert top_k("a b a", -1) == []


# Tests for timetable.py
def test_by_day_groups_and_sorts_courses():
    assert by_day([
        ("CSC10014", "Mon"),
        ("MTH00003", "Tue"),
        ("CSC10001", "Mon"),
    ]) == {
        "Mon": ["CSC10001", "CSC10014"],
        "Tue": ["MTH00003"],
    }


def test_by_day_empty_schedule():
    assert by_day([]) == {}


def test_by_day_same_course_day():
    assert by_day([
        ("CSC10001", "Mon"),
        ("CSC10001", "Mon"),
    ]) == {"Mon": ["CSC10001", "CSC10001"]}


# Tests for translate.py
def test_is_palindrome_simple():
    assert is_palindrome("madam") is True
    assert is_palindrome("hello") is False


def test_is_palindrome_ignores_case_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") is True


def test_is_palindrome_empty_string():
    assert is_palindrome("") is True


def test_is_palindrome_non_palindrome():
    assert is_palindrome("Python!") is False
