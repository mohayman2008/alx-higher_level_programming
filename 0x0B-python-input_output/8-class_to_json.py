#!/usr/bin/python3
"""This module contains the definition of class_to_json()"""


def class_to_json(obj):
    """Returns the dictionary description of an object for JSON serialization
    """
    if "__dict__" not in dir(obj):
        return
    return obj.__dict__
