#!/usr/bin/python3
"""This module contains the definition of function from_json_string()"""
import json


def from_json_string(my_str):
    """Returns a python object represented by a JSON string"""
    json.loads(my_str)
    return eval(str(json.loads(my_str)))
