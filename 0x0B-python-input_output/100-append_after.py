#!/usr/bin/python3
"""This module contains the definition of function append_after_file()"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a
    specific string"""
    if not (filename and search_string):
        return
    s = ""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            s += line
            if line.find(search_string) >= 0:
                s += new_string
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(s)
    pass
