#!/usr/bin/python3
"""defines a json file writing"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using json representation"""
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f, ensure_ascii=False, indent=4)
