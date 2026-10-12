
def binary_search(a: list[int], key: int) -> int:
    """ Search for a key in a sorted list using binary search.

    Unlike C++, Python uses len() for list size
    and // for integer division."""
    lo = 0
    hi = len(a) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if a[mid] == key:
            return mid

        if a[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1
