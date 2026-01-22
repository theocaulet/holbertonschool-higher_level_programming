#!/usr/bin/python3
"""
Function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list of lists of float: A new matrix with all elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
        or if div is not a number.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix:
        length_row: int = len(matrix[0])
    else:
        length_row = 0
    for row in matrix:
        if len(row) != length_row:
            raise TypeError("Each row of the matrix must have the"
                            " same size")
    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)
    return new_matrix
