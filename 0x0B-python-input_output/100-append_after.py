#!/usr/bin/python3
"""defines a text file insertion"""


def append_after(filename="", search_string="", new_string=""):
    """insert text after each line"""
    text = ""
    with open(filename)as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
