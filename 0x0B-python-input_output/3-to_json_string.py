#!/usr/bin/python3

"""
a function that return JSON represent of data
"""
import json


def to_json_string(my_obj):
    """
    returning jsons as obj
    """
    return json.dumps(my_obj)
