#!/usr/bin/python3
"""This module contains the definition of class Student"""


class Student:
    """Definition of Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        pass

    def to_json(self, attrs=None):
        """Returns the dictionary of a Student for JSON serialization"""
        if "__dict__" not in dir(self):
            return
        if type(attrs) is list and all(type(s) is str for s in attrs):
            return {key: self.__dict__[key] for key in attrs
                    if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance based on a dict"""
        if type(json) is not dict:
            return
        if all(type(key) is str for key in json):
            for key, value in json.items():
                setattr(self, key, value)
        pass
    pass
