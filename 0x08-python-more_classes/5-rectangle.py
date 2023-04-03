#!/usr/bin/python3
# 3-rectangle.py by Nebiha Dilsebo
"""defines a rectangle"""


class Rectangle:
    """represents a rectangle"""
    def __init__(self, width=0, height=0):
        """contruct a function using property and setter"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect = ""
            for i in range(self.__height):
                rect += "#" * self.__width
                if i != self.height - 1:
                    rect += "\n"
            return rect

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")

