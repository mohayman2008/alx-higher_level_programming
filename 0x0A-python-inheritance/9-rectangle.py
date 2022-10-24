#!/usr/bin/python3
"""This module contains the definition of the class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry class
    """

    def __init__(self, width, height):
        """Instance initialization"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        pass

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of a Rectangle object"""
        return f"[Rectangle] {self.__width}/{self.__height}"
    pass
