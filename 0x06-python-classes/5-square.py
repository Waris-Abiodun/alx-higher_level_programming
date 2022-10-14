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
        else:
            self.__size = size

    def area(self):
        """Method to get the area of size raise to power 2"""
        return(self.__size ** 2)

    @property
    def size(self):
        """Getter for private size value"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """setter for private size value"""
        if(type(value) is not int):
            raise(TypeError("size must be an integer"))
        elif(value < 0):
            raise(ValueError("size must be >= 0"))
        else:
            self.__size = value

    def my_print(self):
        """A function that print a square using # on the lengtj of size"""i
        if (self.size == 0):
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print("#", end="")
            print()
