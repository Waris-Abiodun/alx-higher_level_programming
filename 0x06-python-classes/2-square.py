#!/usr/bin/python3
"""Square is an empty class with  square size"""


class Square:
    """Square is an empty class with  square size"""

    def __init__(self, size=0):
        """an empty constructor called size"""
        if(type(size) is not int):
            raise(TypeError("size must be an integer"))
        elif(size < 0):
            raise(ValueError("size must be >= 0"))
        self.__size = size
