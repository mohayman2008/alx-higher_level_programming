#!/usr/bin/python3
"""This module contains the definition of function inherits_from()
"""


def inherits_from(obj, a_class):
    """checks if the class of an object is a sub_class of the arbitary class"""
    return type(obj) is not a_class and issubclass(type(obj), a_class)
