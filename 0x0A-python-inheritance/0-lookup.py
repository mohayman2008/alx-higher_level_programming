#!/usr/bin/python3
"""This module contains the definition of function lookup()
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return dir(obj).copy()
