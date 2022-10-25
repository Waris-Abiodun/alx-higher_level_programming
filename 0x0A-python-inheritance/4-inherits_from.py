#!/usr/bin/python3
"""
a function that return if obj and a are of the same class
"""


def inherits_from(obj, a_class):
    """
    a function that return tru if they ae of the same class
    if it is inherit directly or indirectly
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
