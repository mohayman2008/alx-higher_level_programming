#!/usr/bin/python3
"""This module contains the definition of the class Rectangle
"""


class Rectangle:
    """Rectangle class
    """
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle object"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if (not self.height) or (not self.width):
            return 0
        return 2 * (self.height + self.width)

    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        for i in range(2):
            if type((rect_1, rect_2)[i]) is not Rectangle:
                t = ('rect_1', 'rect_2')
                s = f"{t[i]} must be an instance of Rectangle"
                raise TypeError(s)
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return Rectangle(size, size)

    def __str__(self):
        """Returns string representation of the Rectangle object"""
        s = ""
        if self.width and self.height:
            for i in range(self.height):
                s += self.width * str(self.print_symbol) + "\n"
        return s[:-1]

    def __repr__(self):
        """Returns string representation of the Rectangle object
         that can be used to recreate a new Rectangle instance"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Routine to be executed when an object is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        pass
    pass
