
import sys
from pathlib import Path

import pytest

W1_PATH = (
    Path(__file__).resolve().parents[2]
    / "TuanTu2205"
    / "w1"
)
sys.path.insert(0, str(W1_PATH))
from text_tools import word_count, top_k


# Tests for grades.py
from grades import summary


def test_summary_basic_scores():
    assert summary([6.0, 8.0, 10.0]) == {
        "min": 6.0,
        "max": 10.0,
        "mean": 8.0,
        "median": 8.0,
    }


def test_summary_even_number_of_scores():
    assert summary([2.0, 4.0, 6.0, 8.0]) == {
        "min": 2.0,
        "max": 8.0,
        "mean": 5.0,
        "median": 5.0,
    }


def test_summary_single_score():
    assert summary([7.5]) == {
        "min": 7.5,
        "max": 7.5,
        "mean": 7.5,
        "median": 7.5,
    }


def test_summary_rounds_mean_and_median():
    result = summary([1.111, 2.222, 3.333])
    assert result["mean"] == 2.22
    assert result["median"] == 2.22


def test_summary_empty_scores_raises_error():
    import pytest

    with pytest.raises(ValueError, match="scores must not be empty"):
        summary([])


# Tests for rules.py
from rules import can_register_thesis, missing


def test_rules_register_at_minimum_requirements():
    assert can_register_thesis(120, 2.0) is True


def test_rules_reject_insufficient_credits():
    assert can_register_thesis(119, 3.5) is False


def test_rules_reject_low_gpa():
    assert can_register_thesis(130, 1.99) is False


def test_rules_missing_one_credit():
    assert missing(119, 2.5) == [
        "need 1 more credit"
    ]


def test_rules_missing_both_credits_and_gpa():
    assert missing(100, 1.5) == [
        "need 20 more credits",
        "need GPA of at least 2.0",
    ]

# Tests for text_tools.py
from text_tools import word_count, top_k


def test_word_count_ignores_case():
    assert word_count("Python python PYTHON") == {"python": 3}

def test_word_count_punctuation_and_whitespace():
    assert word_count("Hi,  world! Hi.") == {
        "hi": 2,
        "world": 1,
    }

def test_word_count_empty_string():
    assert word_count("") == {}

def test_top_k_orders_by_frequency_then_alphabetically():
    assert top_k("banana apple banana apple cherry", 3) == [
        ("apple", 2),
        ("banana", 2),
        ("cherry", 1),
    ]

def test_top_k_zero_returns_empty_list():
    assert top_k("apple banana", 0) == []

def test_top_k_negative_returns_empty_list():
    assert top_k("apple banana", -1) == []

# Tests for timetable.py
from timetable import by_day

def test_by_day_groups_courses():
    assert by_day([
        ("Math", "Monday"),
        ("English", "Tuesday"),
        ("Physics", "Monday"),
    ]) == {
        "Monday": ["Math", "Physics"],
        "Tuesday": ["English"],
    }

def test_by_day_sorts_courses_alphabetically():
    assert by_day([
        ("Zoology", "Monday"),
        ("Biology", "Monday"),
        ("Math", "Monday"),
    ]) == {
        "Monday": ["Biology", "Math", "Zoology"],
    }

def test_by_day_empty_input():
    assert by_day([]) == {}

# Tests for translate.py
from translate import insertion_sort

def test_insertion_sort_unsorted_list():
    assert insertion_sort([4, 2, 3, 1]) == [1, 2, 3, 4]

def test_insertion_sort_empty_and_single_item():
    assert insertion_sort([]) == []
    assert insertion_sort([5]) == [5]

def test_insertion_sort_duplicates_and_negative_numbers():
    assert insertion_sort([3, -1, 3, 0, -5]) == [-5, -1, 0, 3, 3]
