#!/usr/bin/python3
"""This module contains the definition of function read_file()
"""


def read_file(filename=""):
    """Reads a text file encoded in (UTF8) and prints it to stdout"""
    if not filename:
        return
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
    pass
