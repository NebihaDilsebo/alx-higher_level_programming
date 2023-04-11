#!/usr/bin/python3
"""reads a file"""


def read_file(filename=""):
    """reads textfile and prints to stdout"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
