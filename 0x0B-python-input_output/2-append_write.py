#!/usr/bin/python3
"""This module contains the definition of function append_write()
"""


def append_write(filename="", text=""):
    """Appends a string to a text file encoded in (UTF8)
    and returns the number of characters added"""
    if not filename:
        return 0
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
    pass
