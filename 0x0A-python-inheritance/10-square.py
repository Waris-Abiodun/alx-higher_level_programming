#!/usr/bin/python3

"""
a class that inherits rectangle then also basegeometry cause
rectangle inherits asegeometry
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    this inherits rectangle
    """
    def __init__(self, size):
        """
        this check if size is an intgere or not
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        a function tha square size
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        afunction that return a sttring
        """
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__size, self.__size))
