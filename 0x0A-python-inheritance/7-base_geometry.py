#!/usr/bin/python3
"""this is a class BaseGeometry module"""


class BaseGeometry:
    """this is class"""

    def area(self):
        """calculates area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate if num is integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
