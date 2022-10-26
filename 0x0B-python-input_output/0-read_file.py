#!/usr/bin/python3
"""
a function that read text from a file
"""


def read_file(filename=""):
    """
    open a file and read it cntent
    """
    with open("my_file_0.txt", encoding="UTF8") as myfile:
        print(myfile.read(), end="")
