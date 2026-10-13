"""
Translation and searching utilities for Week 1.
"""

def binary_search(arr: list, target) -> int:
    """Perform binary search on a sorted list to find the target element."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1