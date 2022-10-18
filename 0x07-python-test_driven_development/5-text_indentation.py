#!/usr/bin/python3
"""
a function that use delimeter to read a text
"""
def text_indentation(text):
    """
    a function that read a file using delimeter of\
            '.', '?', ':' followed by two new lines
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    setters = 1
    for words in text:
        for chars in words:
            if (chars is '.' or chars is '?' or chars is ':'):
                print(chars)
                print()
                setters = 0
            elif(setters == 0):
                setters = 1
                continue
            else:
                print("{:s}".format(chars), end="")
