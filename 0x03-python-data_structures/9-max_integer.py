#!/usr/bin/python3
def max_integer(my_list=[]):
     """
     find the maximum value of a list
     Args:
        my_list - list to search
    Return:
        None - if list is empty
        maximum of list
    """
    if my_list is None:
        return None
    i = 0
    while (i < len(my_list) - 1):
        if (my_list[i] > my_list[i + 1]):
            temp = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = temp
        i += 1
    return my_list[i]
