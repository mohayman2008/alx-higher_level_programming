#!/usr/bin/python3
"""This module contains the definition of pascal_triangle()"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s triangle
    """
    if n <= 0:
        return []
    pt = [[1]]
    for row in range(1, n):
        new = pt[-1][:1]
        for i in range(1, row):
            new.append(pt[-1][i - 1] + pt[-1][i])
        new.append(pt[-1][-1])
        pt.append(new)
    return pt
