import pytest

from members.dmdung2520.w1.grades import summary
from members.dmdung2520.w1.rules import can_register_thesis
from members.dmdung2520.w1.text_tools import top_k, word_count
from members.dmdung2520.w1.translate import sieve


def test_grades_summary():
    result = summary([6, 7, 8, 9])
    assert result["mean"] == 7.5
    assert result["median"] == 7.5


def test_grades_empty():
    with pytest.raises(ValueError):
        summary([])


def test_word_count():
    assert word_count("Git git Python!") == {
        "git": 2,
        "python": 1,
    }


def test_top_k_tie():
    assert top_k("apple banana apple banana", 1) == [
        ("apple", 2)
    ]


def test_thesis_boundary():
    assert can_register_thesis(120, 2.0) is True
    assert can_register_thesis(119, 2.0) is False


def test_sieve():
    assert sieve(10) == [2, 3, 5, 7]


def test_sieve_edge_case():
    assert sieve(0) == []
    assert sieve(1) == []
    assert sieve(2) == [2]