#!/usr/bin/python3
"""This module contains the definition of the class MagicClass
"""
import math


class MagicClass:
    """MagicClass
    """
    def __init__(self, radius):
        """Initialize the MagicClass object
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Returns the area of the MagicClass
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Returns the circumference of the MagicClass
        """
        return 2 * math.pi * self.__radius
    pass
