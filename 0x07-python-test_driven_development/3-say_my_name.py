#!/usr/bin/python3
"""
a function that print my name is first and last name
"""


def say_my_name(first_name, last_name=""):
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("my name is {:s} {:s}".format(first_name, last_name))
