#!/usr/bin/python3
"""This module contains the definition of function is_kind_of_class()
"""


def is_kind_of_class(obj, a_class):
    """checks if an object is an instance of an arbitary class or
    if it's class is sub_class of the arbitary class"""
    return issubclass(type(obj), a_class)
