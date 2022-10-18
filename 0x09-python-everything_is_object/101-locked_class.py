#!/usr/bin/python3
"""Module containing the definition of LockedClass"""


class LockedClass:
    """Class not allowing any attribute except it's name is "first_name\""""

    __slots__ = ["first_name"]
    pass
