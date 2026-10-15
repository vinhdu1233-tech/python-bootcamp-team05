"""Translation and sorting utilities for Week 1.

Provides implementation for Bubble Sort algorithm with edge-case handling.

Python vs. C++:
- Python uses len(arr) to get the list length, while C++ commonly
uses size() for containers such as vector.
- Python can swap elements using tuple assignment, while C++ commonly
uses std::swap().
- Python uses dynamic typing, while C++ uses static typing.
- Both languages can implement Bubble Sort with O(n^2) time complexity.
"""


def bubble_sort(arr: list) -> list:
    """Sort a list of elements in ascending order using the bubble sort algorithm.

    Parameters:
        arr (list): A list of comparable elements (e.g., numbers or strings).

    Returns:
        list: A new sorted list in ascending order. If the input list is empty
              or contains a single element, it returns the list as-is.

    Examples:
        >>> bubble_sort([3, 1, 2])
        [1, 2, 3]
        >>> bubble_sort([])
        []
    """
    n = len(arr)
    a = list(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a