#!/usr/bin/python3
"""Square is an empty class with  square size"""


class Square:
    """Square is an empty class with  square size"""

    def __init__(self, size=0, position=(0, 0)):
        """constructor using size and position"""
        if(type(size) is not int):
            raise(TypeError("size must be an integer"))
        elif(size < 0):
            raise(ValueError("size must be >= 0"))
        elif(type(position is not tuple \
                or position[0] and position[1] is int \
                or len(position) != 2 \
                or position[0] < 0 \
                or position[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

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

    @property
    def position(self):
        """a fuction that get the return the postions by setter"""
        return self.__position

    @position.setter
    def position(self, value):
        """ a function that sets value for positions"""
        if (len(value) != 2) or (type(value) is not tuple) \
                or (type(value[0]) is not int) \
                or (type(value[1]) is not int) \
                or (value[0] < 0) or (value[1] < 0):

            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """A function that print a square using # on the lengtj of size"""
        if (self.__size == 0):
            print()
        else:
            for b in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0])
                print("#" * self.__size)
