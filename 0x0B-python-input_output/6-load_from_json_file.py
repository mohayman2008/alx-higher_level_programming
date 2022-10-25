#!/usr/bin/python3
"""This module contains the definition of load_from_json_file()"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file"""
    if type(filename) is not str:
        return
    with open(filename, "r", encoding="utf-8") as my_file:
        return json.load(my_file)
    pass
