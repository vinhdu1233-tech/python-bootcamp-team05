def binary_search(a: list[int], key: int) -> int:
    """Python uses lists instead of C++ vectors and supports type hints."""
    lo, hi = 0, len(a) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if a[mid] == key:
            return mid
        if a[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1
