"""Translation and sorting utilities for Week 1.

Provides implementation for Bubble Sort with edge-case handling.

Python vs. C++:
- Python uses len(arr) to get the list length, while C++ commonly uses
  size() for containers such as vector.
- Python can swap elements using tuple assignment, while C++ commonly
  uses std::swap().
- Python uses dynamic typing, while C++ uses static typing.
- Both languages can implement Bubble Sort with O(n^2) time complexity.
"""

from typing import TypeVar

T = TypeVar("T")


def bubble_sort(arr: list[T]) -> list[T]:
    """Return a new list sorted in ascending order using Bubble Sort.

    The input list is not modified. Elements must support comparison with
    one another.

    Args:
        arr: A list of comparable elements, such as numbers or strings.

    Returns:
        A new sorted list. Empty and single-element lists are also copied.
    """
    n = len(arr)
    result = list(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result
