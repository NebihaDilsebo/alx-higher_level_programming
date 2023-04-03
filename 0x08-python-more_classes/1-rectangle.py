#!/usr/bin/python3
# 1-rectangle.py by Nebiha Dilsebo
"""defines a rectangle"""


class Rectangle:
    """represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
        Args: width - represents the width of the rectangle defined
        and height - represents the height of the rectangle defined
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(width, int):
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
                    if not isinstance(height, int):
                        raise TypeError("height must be an integer")
                    elif value < 0:
                        raise ValueError("height must be >= 0")
                    else:
                        self.__height = value
