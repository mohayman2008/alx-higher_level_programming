#!/usr/bin/python3
"""This module contains the definition of the class Square
"""


class Square:
    """Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square object
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Returns the value of attribute 'position'
        """
        return self.__position

    @position.setter
    def position(self, position):
        """Sets the value of attribute 'position'
        """
        if not isinstance(position, tuple) or len(position) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(not isinstance(val, int) or val < 0 for val in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = (position[0], position[1])

    def area(self):
        """Returns the area of the square
        """
        return self.size ** 2

    def my_print(self):
        """Prints the square using blocks of "#" to stdout
        """
        if self.size == 0:
            print()
            return
        print(self.position[1] * '\n', end="")
        for i in range(self.size):
            print(self.position[0] * ' ' + self.size * "#")

    pass
