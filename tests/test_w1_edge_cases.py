
"""Edge-case tests for all six Week 1 algorithm variants.

Expected module paths:
python-bootcamp/members/<username>/w1/<algorithm>.py

Expected function names:
1. binary_search(arr, target)
2. insertion_sort(arr)
3. transpose(matrix)
4. sieve(n)
5. bubble_sort(arr)
6. is_palindrome(text)

Adjust the module paths, function names, or expected results
if the team agrees on a different interface.
"""

import importlib.util
from pathlib import Path

import pytest

PROJECT_DIR = Path(__file__).resolve().parents[1]
MEMBERS_DIR = PROJECT_DIR / "members"


def load_function(username, module_name, function_name):
    """Load a member's function, or skip if their code is not ready."""
    path = MEMBERS_DIR / username / "w1" / f"{module_name}.py"

    if not path.exists():
        pytest.skip(f"Implementation not available yet: {path}")

    spec = importlib.util.spec_from_file_location(
        f"{username}_{module_name}", path
    )

    if spec is None or spec.loader is None:
        pytest.fail(f"Cannot load module: {path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, function_name):
        pytest.skip(
            f"Function {function_name}() is not implemented yet in {path}"
        )

    return getattr(module, function_name)


# ============================================================
# VARIANT 1 — vinhdu1233-tech
# Binary Search
# Contract: return an index when found, otherwise -1.
# Input list must be sorted.
# ============================================================

def test_v1_binary_search_empty_list():
    binary_search = load_function(
        "vinhdu1233-tech", "binary_search", "binary_search"
    )
    assert binary_search([], 5) == -1


def test_v1_binary_search_single_element_found():
    binary_search = load_function(
        "vinhdu1233-tech", "binary_search", "binary_search"
    )
    assert binary_search([7], 7) == 0


def test_v1_binary_search_single_element_missing():
    binary_search = load_function(
        "vinhdu1233-tech", "binary_search", "binary_search"
    )
    assert binary_search([7], 3) == -1


def test_v1_binary_search_first_and_last_elements():
    binary_search = load_function(
        "vinhdu1233-tech", "binary_search", "binary_search"
    )
    values = [1, 3, 5, 7, 9]

    assert binary_search(values, 1) == 0
    assert binary_search(values, 9) == 4


def test_v1_binary_search_duplicate_values():
    binary_search = load_function(
        "vinhdu1233-tech", "binary_search", "binary_search"
    )
    values = [1, 3, 5, 5, 5, 8]
    index = binary_search(values, 5)

    assert index in (2, 3, 4)
    assert values[index] == 5


# ============================================================
# VARIANT 2 — TuanTu2205
# Insertion Sort
# Contract: return a new sorted list or sort in-place.
# These tests assume the function returns the sorted list.
# ============================================================

def test_v2_insertion_sort_empty_list():
    insertion_sort = load_function(
        "TuanTu2205", "insertion_sort", "insertion_sort"
    )
    assert insertion_sort([]) == []


def test_v2_insertion_sort_single_element():
    insertion_sort = load_function(
        "TuanTu2205", "insertion_sort", "insertion_sort"
    )
    assert insertion_sort([42]) == [42]


def test_v2_insertion_sort_already_sorted():
    insertion_sort = load_function(
        "TuanTu2205", "insertion_sort", "insertion_sort"
    )
    assert insertion_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_v2_insertion_sort_reverse_order():
    insertion_sort = load_function(
        "TuanTu2205", "insertion_sort", "insertion_sort"
    )
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_v2_insertion_sort_duplicates_and_negative_numbers():
    insertion_sort = load_function(
        "TuanTu2205", "insertion_sort", "insertion_sort"
    )
    assert insertion_sort([3, -1, 3, 0, -1]) == [-1, -1, 0, 3, 3]


# ============================================================
# VARIANT 3 — tree312-coder
# Matrix Transpose
# Contract: transpose a rectangular matrix represented by lists.
# ============================================================

def test_v3_transpose_empty_matrix():
    transpose = load_function(
        "tree312-coder", "matrix_transpose", "transpose"
    )
    assert transpose([]) == []


def test_v3_transpose_single_element():
    transpose = load_function(
        "tree312-coder", "matrix_transpose", "transpose"
    )
    assert transpose([[7]]) == [[7]]


def test_v3_transpose_single_row():
    transpose = load_function(
        "tree312-coder", "matrix_transpose", "transpose"
    )
    assert transpose([[1, 2, 3]]) == [[1], [2], [3]]


def test_v3_transpose_single_column():
    transpose = load_function(
        "tree312-coder", "matrix_transpose", "transpose"
    )
    assert transpose([[1], [2], [3]]) == [[1, 2, 3]]


def test_v3_transpose_rectangular_matrix():
    transpose = load_function(
        "tree312-coder", "matrix_transpose", "transpose"
    )
    matrix = [[1, 2, 3], [4, 5, 6]]

    assert transpose(matrix) == [
        [1, 4],
        [2, 5],
        [3, 6],
    ]


# ============================================================
# VARIANT 4 — dmdung2520
# Sieve of Eratosthenes
# Contract: return all primes <= n in ascending order.
# ============================================================

def test_v4_sieve_below_two():
    sieve = load_function(
        "dmdung2520", "sieve", "sieve"
    )
    assert sieve(0) == []
    assert sieve(1) == []


def test_v4_sieve_smallest_prime():
    sieve = load_function(
        "dmdung2520", "sieve", "sieve"
    )
    assert sieve(2) == [2]


def test_v4_sieve_three():
    sieve = load_function(
        "dmdung2520", "sieve", "sieve"
    )
    assert sieve(3) == [2, 3]


def test_v4_sieve_prime_boundary():
    sieve = load_function(
        "dmdung2520", "sieve", "sieve"
    )
    assert sieve(10) == [2, 3, 5, 7]


def test_v4_sieve_square_boundary():
    sieve = load_function(
        "dmdung2520", "sieve", "sieve"
    )
    assert sieve(25) == [2, 3, 5, 7, 11, 13, 17, 19, 23]


# ============================================================
# VARIANT 5 — fumeneko
# Bubble Sort
# Contract: return the sorted list.
# ============================================================

def test_v5_bubble_sort_empty_list():
    bubble_sort = load_function(
        "fumeneko", "bubble_sort", "bubble_sort"
    )
    assert bubble_sort([]) == []


def test_v5_bubble_sort_single_element():
    bubble_sort = load_function(
        "fumeneko", "bubble_sort", "bubble_sort"
    )
    assert bubble_sort([9]) == [9]


def test_v5_bubble_sort_already_sorted():
    bubble_sort = load_function(
        "fumeneko", "bubble_sort", "bubble_sort"
    )
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_v5_bubble_sort_reverse_order():
    bubble_sort = load_function(
        "fumeneko", "bubble_sort", "bubble_sort"
    )
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_v5_bubble_sort_duplicates_and_negative_numbers():
    bubble_sort = load_function(
        "fumeneko", "bubble_sort", "bubble_sort"
    )
    assert bubble_sort([0, -5, 2, -5, 2]) == [-5, -5, 0, 2, 2]


# ============================================================
# VARIANT 6 — lnmthi
# Palindrome Checker
# Contract: check whether the exact input string is a palindrome.
# Case and punctuation are significant in this version.
# ============================================================

def test_v6_palindrome_empty_string():
    is_palindrome = load_function(
        "lnmthi", "palindrome", "is_palindrome"
    )
    assert is_palindrome("")


def test_v6_palindrome_single_character():
    is_palindrome = load_function(
        "lnmthi", "palindrome", "is_palindrome"
    )
    assert is_palindrome("a")


def test_v6_palindrome_even_length():
    is_palindrome = load_function(
        "lnmthi", "palindrome", "is_palindrome"
    )
    assert is_palindrome("abba")


def test_v6_palindrome_odd_length():
    is_palindrome = load_function(
        "lnmthi", "palindrome", "is_palindrome"
    )
    assert is_palindrome("racecar")


def test_v6_non_palindrome():
    is_palindrome = load_function(
        "lnmthi", "palindrome", "is_palindrome"
    )
    assert not is_palindrome("hello")


def test_v6_case_sensitive_behavior():
    is_palindrome = load_function(
        "lnmthi", "palindrome", "is_palindrome"
    )
    assert not is_palindrome("Racecar")
