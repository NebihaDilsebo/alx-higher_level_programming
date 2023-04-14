#!/usr/bin/python3
"""adds all arguments to a Python list"""
import sys
import json
import os import path
from typing import list

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNiotFoundError:
        my_list = []
        my_list.extend(sys.argv[1:])
        save_to_json_file(my_list, "add_item.json") 
