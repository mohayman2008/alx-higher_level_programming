#!/usr/bin/python3
"""This module contains the definition of the Base class"""


class Base:
    """Definition of the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Objects of class Base constructor"""
        if id is None:
            self.__class__.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
        pass
    pass
