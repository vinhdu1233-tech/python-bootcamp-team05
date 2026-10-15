def insertion_sort(a: list[int]) -> list[int]:
    """Sort a list in place using insertion sort.

    Unlike C++, Python lists do not require explicit variable type declarations for loop indices.
    """

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >=0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1

        a[j+1] = key
    
    return a