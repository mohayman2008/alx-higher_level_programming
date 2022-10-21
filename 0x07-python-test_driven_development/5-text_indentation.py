#!/usr/bin/python3
"""This module contains the definition of text_indentation()
"""


def text_indentation(text):
    """Prints a text with 2 new lines after every '.', '?' and ':'"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.strip()
    for a in (".", "?", ":"):
        ax = a + ' '
        new = text.replace(ax, a)
        while new != text:
            text = new
            new = text.replace(ax, a)
        text = text.replace(a, a + "\n\n")
    print(text, end="")
    pass
