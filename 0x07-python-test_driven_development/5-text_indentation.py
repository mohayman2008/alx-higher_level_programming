#!/usr/bin/python3
"""This module contains the definition of text_indentation()
"""


def text_indentation(text):
    """Prints a text with 2 new lines after every '.', '?' and ':'"""

    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip()
    text = text.replace(".", ".\n\n").replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    print(text, end="")
    pass
