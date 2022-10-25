#!/usr/bin/python3
"""This module contains the definition of save_to_json_file()"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""
    if type(filename) is not str:
        return
    with open(filename, "w", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
    pass
