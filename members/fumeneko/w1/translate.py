"""Translation and sorting utilities for Week 1.

Provides implementation for Bubble Sort algorithm with edge-case handling.
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