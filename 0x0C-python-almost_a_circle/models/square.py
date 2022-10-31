#!/usr/bin/python3
"""This module contains the definition of the Rectangle class"""
try:
    from . import Base, Rectangle
except ImportError:
    from base import Base
    from rectangle import Rectangle


class Square(Rectangle):
    """Definition of the Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square object constructor"""
        super().__init__(size, size, x, y, id)
        pass

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size
        pass

    def update(self, *args, **kwargs):
        """Updating Square object by assigning arguments to their
        respective attribute"""
        if not len(args):
            for key, value in kwargs.items():
                if key in ('id', 'size', 'x', 'y'):
                    setattr(self, key, value)
        else:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        pass

    def __str__(self):
        """Returns the string representation of a Square object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
    pass
