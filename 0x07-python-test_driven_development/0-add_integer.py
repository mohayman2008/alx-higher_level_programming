#!/usr/bin/python3
"""This module contains the definition of add_integer
"""


def add_integer(a, b=98):
    """Add two integers a and b"""

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
