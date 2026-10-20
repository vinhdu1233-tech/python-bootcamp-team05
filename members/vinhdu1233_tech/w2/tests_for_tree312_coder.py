
import pytest

from members.tree312_coder.w1.grades import summary
from members.tree312_coder.w1.rules import can_register_thesis
from members.tree312_coder.w1.text_tools import top_k, word_count
from members.tree312_coder.w1.timetable import by_day
from members.tree312_coder.w1.translate import transpose


def test_grade_summary():
    result = summary([6, 8, 10])

    assert result["min"] == 6
    assert result["max"] == 10
    assert result["mean"] == 8
    assert result["median"] == 8


def test_empty_scores():
    with pytest.raises(ValueError):
        summary([])


def test_word_count():
    result = word_count("Python, python! Git.")

    assert result == {"python": 2, "git": 1}


def test_top_k():
    result = top_k("cat dog cat bird dog cat", 2)

    assert result == [("cat", 3), ("dog", 2)]


def test_thesis_eligibility():
    assert can_register_thesis(120, 2.0) is True
    assert can_register_thesis(119, 2.0) is False


def test_timetable_sorting():
    data = [
        ("MTH00003", "Mon"),
        ("CSC10014", "Mon"),
    ]

    assert by_day(data) == {
        "Mon": ["CSC10014", "MTH00003"]
    }


def test_transpose_empty_matrix():
    """Additional candidate edge case: empty matrix."""
    assert transpose([]) == []
