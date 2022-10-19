#!/usr/bin/python3
"""This module contains the definition of lazy_matrix_mul()
"""
import numpy as np

"""
def matrix_mul(m_a, m_b):
    """'Multiplies 2 matrices'"""

    names = ("m_a", "m_b")
    for i, matrix in enumerate((m_a, m_b)):
        if type(matrix) is not list:
            raise TypeError(f"{names[i]} must be a list")
    for i, matrix in enumerate((m_a, m_b)):
        if any(type(r) is not list for r in matrix):
            raise TypeError(f"{names[i]} must be a list of lists")
    for i, matrix in enumerate((m_a, m_b)):
        if not len(matrix) or matrix == [[]]:
            raise ValueError(f"{names[i]} can't be empty")
    for i, matrix in enumerate((m_a, m_b)):
        for row in matrix:
            if any(type(col) not in (int, float) for col in row):
                s = f"{names[i]} should contain only integers or floats"
                raise TypeError(s)
    for i, matrix in enumerate((m_a, m_b)):
        if any(len(r) != len(matrix[0]) for r in matrix[1:]):
            raise TypeError(f"each row of {names[i]} must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            c = sum([m_a[i][k] * m_b[k][j] for k in range(len(m_b))])
            row.append(c)
        result.append(row)
    return result
"""

def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices using NumPy"""

    m_a, m_b = (np.array(m_a), np.array(m_b))

    """names = ("m_a", "m_b")
    for i, matrix in enumerate((m_a, m_b)):
        if type(matrix) is not list:
            raise TypeError(f"{names[i]} must be a list")
    for i, matrix in enumerate((m_a, m_b)):
        if any(type(r) is not list for r in matrix):
            raise TypeError(f"{names[i]} must be a list of lists")
    for i, matrix in enumerate((m_a, m_b)):
        if not len(matrix) or matrix == [[]]:
            raise ValueError(f"{names[i]} can't be empty")
    for i, matrix in enumerate((m_a, m_b)):
        for row in matrix:
            if any(type(col) not in (int, float) for col in row):
                s = f"{names[i]} should contain only integers or floats"
                raise TypeError(s)
    for i, matrix in enumerate((m_a, m_b)):
        if any(len(r) != len(matrix[0]) for r in matrix[1:]):
            raise TypeError(f"each row of {names[i]} must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            c = sum([m_a[i][k] * m_b[k][j] for k in range(len(m_b))])
            row.append(c)
        result.append(row)
"""
    result = np.matmul(m_a, m_b)
    return result
