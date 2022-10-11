#!/usr/bin/python3
"""This module contains the definition of the class Square
"""


class Square:
    """Square class
    """
    def __init__(self, size=0):
        """Initialize the square object
        """
        self.size = size

    @property
    def size(self):
        """Returns the value of attribute 'size'
        """
        return self.__size

    @size.setter
    def size(self, size):
        """Sets the value of attribute 'size'
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
        return self.size ** 2

    def __eq__(self, other):
        """This method will be called when '==' operator is used
        """
        return isinstance(other, Square) and self.area() == other.area()

    def __lt__(self, other):
        """This method will be called when '<' operator is used
        """
        return isinstance(other, Square) and self.area() < other.area()

    def __le__(self, other):
        """This method will be called when '<=' operator is used
        """
        return isinstance(other, Square) and self.area() <= other.area()

    def __ne__(self, other):
        """This method will be called when '!=' operator is used
        """
        return isinstance(other, Square) and self.area() != other.area()

    def __gt__(self, other):
        """This method will be called when '>' operator is used
        """
        return isinstance(other, Square) and self.area() > other.area()

    def __ge__(self, other):
        """This method will be called when '>=' operator is used
        """
        return isinstance(other, Square) and self.area() >= other.area()
    pass
