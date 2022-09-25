#!/usr/bin/python3
def print_list_integer(my_list=[]):
    i = 0
    b = my_list
    while (i < len(b)):
        print("{:d}".format(b[i]))
        i += 1
