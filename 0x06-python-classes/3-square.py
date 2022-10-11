#!/usr/bin/python3
"""This module contains the definition of the class Square
"""


class Square:
    """Square class
    """
    def __init__(self, size=0):
        """Initialize the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the area of the square
        """
        return self.__size ** 2
    pass
