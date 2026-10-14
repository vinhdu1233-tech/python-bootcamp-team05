
def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Return the transpose of a matrix.

    In C++, we usually use nested loops and indexes to access
    matrix elements. In Python, zip(*matrix) combines elements
    at the same position from different rows, making the code
    shorter and easier to read.
    """
    return [list(row) for row in zip(*matrix)]
