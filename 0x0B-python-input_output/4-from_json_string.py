#!/usr/bin/python3
"""This module contains the definition of function from_json_string()"""
import json


def from_json_string(my_str):
    """Returns a python object represented by a JSON string"""
    if type(my_str) is not str:
        return
    return eval(str(json.loads(my_str)))
