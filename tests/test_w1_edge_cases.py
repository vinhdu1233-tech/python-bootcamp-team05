"""Comprehensive test cases for all team members based on variants."""


def test_w1_team_all_members(load, variant):
    """Test cases covering all modules and team members' algorithms."""
    g = load("w1", "grades")
    assert g.process_grades([]) is not None

    t = load("w1", "text_tools")
    assert t.word_count("") == {}
    assert t.top_k("hello world", 2) == [("hello", 1), ("world", 1)]

    r = load("w1", "rules")
    assert r.can_register_thesis(0, 0.0) is False
    assert r.missing(50, 1.0) is not None

    tt = load("w1", "timetable")
    assert tt.by_day([]) == {}

    tr = load("w1", "translate")
    if variant == 1:
        if hasattr(tr, "binary_search"):
            assert tr.binary_search([1, 3, 5, 7], 5) == 2
            assert tr.binary_search([], 5) == -1
    elif variant == 2:
        if hasattr(tr, "insertion_sort"):
            assert tr.insertion_sort([3, 1, 2]) == [1, 2, 3]
            assert tr.insertion_sort([]) == []
    elif variant == 3:
        if hasattr(tr, "transpose"):
            assert tr.transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
            assert tr.transpose([]) == []
    elif variant == 4:
        if hasattr(tr, "primes_up_to"):
            assert tr.primes_up_to(10) == [2, 3, 5, 7]
            assert tr.primes_up_to(1) == []
    elif variant == 5:
        if hasattr(tr, "bubble_sort"):
            assert tr.bubble_sort([3, 1, 2]) == [1, 2, 3]
            assert tr.bubble_sort([]) == []
    else:
        if hasattr(tr, "is_palindrome"):
            assert tr.is_palindrome("racecar") is True
            assert tr.is_palindrome("hello") is False