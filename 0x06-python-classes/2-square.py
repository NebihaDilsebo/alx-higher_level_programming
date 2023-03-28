#!/usr/bin/python3
# 0-square.py by Nebiha Dilsebo
"""a module that defines a square """


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """initializing this square class
        Args:
        size: represents the size of the squaredefined
        Raises:
        TypeError: if size is not intiger
        ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an intiger')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
         

