#!/usr/bin/python3
"""This module contains the definition of the class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle class
    """

    def __init__(self, size):
        """Instance initialization"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
        pass

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__size ** 2

    def __str__(self):
        """Returns a Square's string representation"""
        return f"[Square] {self.__size}/{self.__size}"
    pass
