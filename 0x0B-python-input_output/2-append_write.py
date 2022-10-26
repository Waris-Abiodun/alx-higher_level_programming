#!/usr/bin/python3
"""
a function that read text from a file
"""


def append_write(filename="", text=""):
    """
    open a file and write to it
    """
    with open(filename, mode='a', encoding="UTF8") as myfile:
        wordcount = myfile.write(text)
    return wordcount
