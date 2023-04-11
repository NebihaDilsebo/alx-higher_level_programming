#!/usr/bin/python3
"""defines a string to json function"""
import json


def to_json_string(my_obj):
    """return the json representation of string"""
    return json.dumps(my_obj)
