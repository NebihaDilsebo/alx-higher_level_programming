#!/usr/bin/python3
""" append write"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file"""
    with open(filename, mode='a', encoding='utf8') as f:
        return f.write(text)
