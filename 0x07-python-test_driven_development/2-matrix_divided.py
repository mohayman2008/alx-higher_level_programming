#!/usr/bin/python3
"""This module contains the definition of matrix_divided()
"""


def matrix_divided(matrix, div):
    """Divides the elements of a Matrix by arbitary number"""

    if type(matrix) is not list or any(type(r) is not list for r in matrix):
        s = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(s)
    if any(len(r) != len(matrix[0]) for r in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        if any(type(col) not in (int, float) for col in row):
            s = "matrix must be a matrix (list of lists) of integers/floats"
            raise TypeError(s)
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(col / div, 2) for col in row] for row in matrix]
