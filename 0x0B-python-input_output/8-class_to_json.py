#!/usr/bin/python3
"""defines a class to join to-json function"""


def class_to_json(obj):
    """get direction of objects attribute"""
    attrs = vars(obj)

    """creates empty dictionary for serialized object"""
    serialized_obj = {}

    """serializ attributes"""
    for key, value in attrs.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized_obj[key] = value

    return serialized_obj
