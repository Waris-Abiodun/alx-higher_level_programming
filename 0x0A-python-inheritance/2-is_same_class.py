#!/usr/bin/python3
"""
a function that return if obj and a are of the same class
"""


def is_same_class(obj, a_class):
    """
    a function that return tru if they ae of the same class
    """
    if type(obj) == a_class:
        return True
    return False
