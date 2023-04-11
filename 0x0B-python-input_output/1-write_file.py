#!/usr/bin/python3
"""writes file"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, mode='w', encoding='utf8') as f:
        return f.write(text)
