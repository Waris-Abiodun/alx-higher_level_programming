#!/usr/bin/python3
"""
a function that print square
"""


def print_square(size):
    """checking condition before printing the square"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
