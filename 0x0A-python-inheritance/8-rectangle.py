#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" this ia a class rectangle module"""


class Rectangle(BaseGeometry):
    """Rectangle class from BaseGeometry"""

    def __init__(self, width, height):
        self.intiger_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
