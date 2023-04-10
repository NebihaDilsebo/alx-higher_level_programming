#!/usr/bin/python3
""" module 0-lookup
this is a list of available attributes and method of an object"""


def lookup(obj):
    """Returns a list of object
    Args:
        any object
        returns:
            a list"""
    return dir(obj)
