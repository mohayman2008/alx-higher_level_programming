#!/usr/bin/python3
"""This module contains the definition of the class Rectangle
"""


class Rectangle:
    """Rectangle class
    """
    def __init__(self, width=0, height=0):
        """Initialize the Rectangle object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the value of attribute 'width'"""
        return self.__width

    @width.setter
    def width(self, width):
        """Returns the value of attribute 'width'"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Returns the value of attribute 'height'"""
        return self.__height

    @height.setter
    def height(self, height):
        """Returns the value of attribute 'height'"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
    pass
