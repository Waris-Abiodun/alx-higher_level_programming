#!/usr/bin/python3

"""
a function that returns attribute of a class
"""


def lookup(obj):
    """
    a function that return the attribut of a class using dir
    it return the list
    Args:
        obj(any) : object whose attribute will be returned
    """

    return (dir(obj))
