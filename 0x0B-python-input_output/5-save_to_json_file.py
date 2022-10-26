#!/usr/bin/python3

"""
a function that return JSON represent of data
"""
import json


def save_to_json_file(my_obj, filename):
    """
    returning jsons as obj
    """
    with open(filename, 'w') as myfile:
        json.dump(obj, myfile)
