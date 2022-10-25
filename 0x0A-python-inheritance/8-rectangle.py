#!/usr/bin/python3
"""
a function that inherits geometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a function that use int validator in geometry to check for the
    width and height of the rectangle
    """

    def __init__(self, width, height):
        """
        check for width and height and allocate value for them
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
