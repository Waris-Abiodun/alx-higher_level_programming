#!/usr/bin/python3
"""
a class that work
"""


class BaseGeometry:
    """
    an classs that has many
    """

    def area(self):
        """
        a function that raises an error that its not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        a function that fve th following
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
