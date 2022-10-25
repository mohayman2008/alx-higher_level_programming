#!/usr/bin/python3
"""This module contains the definition of function write_file()
"""


def write_file(filename="", text=""):
    """Writes a string to a text file encoded in (UTF8)
    and returns the number of characters written"""
    if not filename:
        return 0
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
    pass
