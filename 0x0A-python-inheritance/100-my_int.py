#!/usr/bin/python3
"""This module contains the definition of the class MyInt
"""


class MyInt(int):
    """MyInt class
    """

    def __eq__(self, other):
        """The handler for the '==' operator"""
        return int(self) != int(other)

    def __ne__(self, other):
        """The handler for the '!=' operator"""
        return int(self) == int(other)
    pass
