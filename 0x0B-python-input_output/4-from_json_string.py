#!/usr/bin/python3

"""
a function that return JSON represent of data
"""
import json


def from_json_string(my_str):
    """
    returning jsons as obj
    """
    return json.loads(my_str)
