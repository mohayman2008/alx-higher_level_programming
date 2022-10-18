#!/usr/bin/python3
"""This module contains the definition of def print_square()
"""


def print_square(size):
    """Prints a square using the character '#'"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
    pass
