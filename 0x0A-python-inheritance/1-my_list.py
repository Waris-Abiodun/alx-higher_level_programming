#!/usr/bin/python3
"""
a function that sort a list
"""


class MyList(list):
    """
    mylis inherits list
    """
    def print_sorted(self):
        """
        it assume all arguments are integer and it will sort it
        """
        sortlist = sorted(self)
        print(sortlist)
