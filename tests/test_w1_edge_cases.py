
"""Edge-case tests for the Python Bootcamp Week 1 algorithms.

Expected repository layout:
python-bootcamp/
    members/<username>/w1/translate.py
    tests/test_w1_edge_cases.py

Missing implementations are errors by default. During team integration,
set PY_W1_ALLOW_MISSING=1 to temporarily skip only members whose files
have not been merged yet.
"""

import importlib.util
import os
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
MEMBERS_DIR = ROOT / "members"

ALLOW_MISSING = os.getenv("PY_W1_ALLOW_MISSING") == "1"


IMPLEMENTATIONS = {
    "binary_search": ("vinhdu1233_tech", "binary_search"),
    "insertion_sort": ("TuanTu2205", "insertion_sort"),
    "transpose": ("tree312_coder", "transpose"),
    "sieve": ("dmdung2520", "sieve"),
    "bubble_sort": ("fumeneko", "bubble_sort"),
    "palindrome_checker": ("lnmthi", "is_palindrome"),
}


def load_function(username, function_name):
    """Import a required function from the member's translate.py."""
    path = MEMBERS_DIR / username / "w1" / "translate.py"

    if not path.is_file():
        message = f"Missing implementation file: {path}"

        if ALLOW_MISSING:
            pytest.skip(message)

        pytest.fail(message)

    spec = importlib.util.spec_from_file_location(
        f"week1_{username}_{function_name}", path
    )

    if spec is None or spec.loader is None:
        pytest.fail(f"Cannot load module: {path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    function = getattr(module, function_name, None)

    if not callable(function):
        pytest.fail(
            f"Expected callable {function_name}() in {path}"
        )

    return function


# Fixtures

@pytest.fixture(scope="module")
def binary_search():
    return load_function(*IMPLEMENTATIONS["binary_search"])


@pytest.fixture(scope="module")
def insertion_sort():
    return load_function(*IMPLEMENTATIONS["insertion_sort"])


@pytest.fixture(scope="module")
def transpose():
    return load_function(*IMPLEMENTATIONS["transpose"])


@pytest.fixture(scope="module")
def sieve():
    return load_function(*IMPLEMENTATIONS["sieve"])


@pytest.fixture(scope="module")
def bubble_sort():
    return load_function(*IMPLEMENTATIONS["bubble_sort"])


@pytest.fixture(scope="module")
def palindrome_checker():
    return load_function(*IMPLEMENTATIONS["palindrome_checker"])


# Binary Search

@pytest.mark.parametrize(
    ("values", "target", "expected"),
    [
        ([], 5, -1),
        ([7], 7, 0),
        ([7], 3, -1),
        ([1, 3, 5, 7, 9], 1, 0),
        ([1, 3, 5, 7, 9], 9, 4),
        ([1, 3, 5, 7, 9], 5, 2),
        ([1, 3, 5, 7, 9], 4, -1),
        ([-9, -3, 0, 4], -9, 0),
    ],
)
def test_binary_search_edges(binary_search, values, target, expected):
    assert binary_search(values, target) == expected


# Insertion Sort

@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 3]),
        ([4, 4, 4], [4, 4, 4]),
        ([3, -1, 0, -5], [-5, -1, 0, 3]),
    ],
)
def test_insertion_sort_edges(insertion_sort, values, expected):
    result = insertion_sort(values.copy())
    assert result == expected


# Matrix Transpose

@pytest.mark.parametrize(
    ("matrix", "expected"),
    [
        ([], []),
        ([[1]], [[1]]),
        ([[1, 2, 3]], [[1], [2], [3]]),
        ([[1], [2], [3]], [[1, 2, 3]]),
        ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),
        ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
    ],
)
def test_transpose_edges(transpose, matrix, expected):
    original = [row.copy() for row in matrix]

    assert transpose(matrix) == expected
    assert matrix == original


# Sieve of Eratosthenes

@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (-5, []),
        (0, []),
        (1, []),
        (2, [2]),
        (3, [2, 3]),
        (10, [2, 3, 5, 7]),
        (20, [2, 3, 5, 7, 11, 13, 17, 19]),
    ],
)
def test_sieve_edges(sieve, n, expected):
    assert sieve(n) == expected


# Bubble Sort

@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([2, 2, 1, 2], [1, 2, 2, 2]),
        ([-3, 0, -1, 5], [-3, -1, 0, 5]),
    ],
)
def test_bubble_sort_edges(bubble_sort, values, expected):
    result = bubble_sort(values.copy())
    assert result == expected


# Palindrome Checker

@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("racecar", True),
        ("hello", False),
        ("a", True),
        ("12321", True),
        ("12345", False),
        ("", True),
    ],
)
def test_palindrome_checker_edges(palindrome_checker, value, expected):
    assert palindrome_checker(value) is expected