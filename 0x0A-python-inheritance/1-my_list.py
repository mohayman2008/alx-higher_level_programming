#!/usr/bin/python3
"""This module contains the definition of the class MyList
"""


class MyList(list):
    """MyList class
    """

    def print_sorted(self):
        """Print a sorted version of the list"""
        new = self.copy()
        new.sort()
        print(new)
        pass
    pass
