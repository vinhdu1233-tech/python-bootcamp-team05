
def binary_search(a: list[int], key: int) -> int:
    """Search a sorted list and return the index or -1.

    Python lists support direct indexing, unlike C++ iterators.
    """
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


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9]
    print(binary_search(numbers, 5))   # 2
    print(binary_search(numbers, 4))   # -1
    print(binary_search([], 1))        # -1
