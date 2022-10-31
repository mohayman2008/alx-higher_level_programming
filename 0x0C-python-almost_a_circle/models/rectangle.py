#!/usr/bin/python3
"""This module contains the definition of the Rectangle class"""
try:
    from . import Base
except ImportError:
    from base import Base


class Rectangle(Base):
    """Definition of the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle object constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        pass

    @staticmethod
    def validate_int(name, value):
        """Validate the type of a variable to be integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        pass

    @staticmethod
    def validate_gt0(name, value):
        """Validate that the value of an integer is > 0"""
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))
        pass

    @staticmethod
    def validate_ge0(name, value):
        """Validate that the value of an integer is >= 0"""
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
        pass

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        self.validate_int("width", width)
        self.validate_gt0("width", width)
        self.__width = width
        pass

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        self.validate_int("height", height)
        self.validate_gt0("height", height)
        self.__height = height
        pass

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        self.validate_int("x", x)
        self.validate_ge0("x", x)
        self.__x = x
        pass

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        self.validate_int("y", y)
        self.validate_ge0("y", y)
        self.__y = y
        pass

    def update(self, *args, **kwargs):
        """Updating Rectangle object by that assigning arguments to their
        respective attribute"""
        if not len(args):
            for key, value in kwargs.items():
                if key in ('id', 'width', 'height', 'x', 'y'):
                    setattr(self, key, value)
        else:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        pass

    def area(self):
        """Returns the area of a Rectangle object"""
        return (self.__width * self.__height)

    def display(self):
        """Displays a Rectangle object using '#' character"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)
        pass

    def __str__(self):
        """Returns the string representation of a Rectangle object"""
        s = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
        s += f"{self.__width}/{self.__height}"
        return s

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
    pass
