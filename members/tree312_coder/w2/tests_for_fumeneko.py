
import pytest

from members.fumeneko.w1.grades import summary
from members.fumeneko.w1.rules import can_register_thesis, missing
from members.fumeneko.w1.text_tools import top_k, word_count
from members.fumeneko.w1.timetable import by_day
from members.fumeneko.w1.translate import bubble_sort


def test_word_count_case_insensitive():
    assert word_count("Cat cat DOG") == {"cat": 2, "dog": 1}


def test_word_count_removes_punctuation():
    assert word_count("Hello, hello! world.") == {
        "hello": 2,
        "world": 1,
    }


def test_word_count_empty_text():
    assert word_count("   ") == {}


def test_top_k_sorts_by_frequency_and_alphabetically():
    assert top_k("banana apple banana apple cherry", 3) == [("apple", 2), ("banana", 2), ("cherry", 1),]


def test_top_k_zero():
    assert top_k("cat dog", 0) == []


def test_can_register_thesis():
    assert can_register_thesis(120, 2.0) is True
    assert can_register_thesis(119, 2.0) is False
    assert can_register_thesis(120, 1.99) is False


def test_missing_both_requirements():
    assert missing(115, 1.5) == ["need 5 more credits", "GPA too low",]


def test_summary_even_number_of_scores():
    assert summary([1, 2, 3, 4]) == {"min": 1, "max": 4, "mean": 2.5, "median": 2.5,
    }


def test_summary_empty_scores():
    with pytest.raises(ValueError):
        summary([])


def test_by_day_groups_and_sorts_courses():
    assert by_day([
        ("CS2", "Mon"),
        ("CS1", "Mon"),
        ("MA1", "Tue"),
    ]) == {
        "Mon": ["CS1", "CS2"],
        "Tue": ["MA1"],
    }


def test_bubble_sort_sorts_numbers():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]


def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []
