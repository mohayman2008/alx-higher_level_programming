#!/usr/bin/python3
"""This module contains the definition of the class BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry class
    """

    def __init__(self):
        """Initializer"""
        pass

    def area(self):
        """Blueprint method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(name) is not str:
            raise TypeError("name must be a string")
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
    pass
