#!/usr/bin/python3
"""A function that add two variables"""


def add_integer(a, b=98):
    """ a function that check condition before adding"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
