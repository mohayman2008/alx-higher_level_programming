#!/usr/bin/python3
"""This module contains the definition of function is_same_class()
"""


def is_same_class(obj, a_class):
    """checks if an object is exactly an instance of an arbitary class"""
    return type(obj) is a_class
