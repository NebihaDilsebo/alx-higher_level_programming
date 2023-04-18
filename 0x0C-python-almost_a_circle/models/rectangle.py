#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""module that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """rectangle class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor for rectangle

        Attributes:
            width (int): Private attribute for the width of the rectangle
            height (int):Private attribute for the height of the rectangle
            x (int): Private attribute for x value of the Rectangle
            id (int): Private attribute id inherits from Base"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        """Returns the width of rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle instance"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the height of Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of Rectangle instance"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be an integer')
        else:
            self.__height = value

    @property
    def x(self):
        """Returns the x coordinate of the Rectangle instance"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x coordinate of the Rectangle instance"""
        if not isinstance(value, int):
            raise TypeError('x must be an intiger')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """Returns the y coordinate of the Rectangle instance"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y coordinate of the Rectangle instance"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout"""
        for i in range(self.height):
            print('#' * self.width)

    def __str__(self):
        """str method for class Rectangle

        Return:
            The string: [class_name] (id) x/y - width/height"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} \
                - {self.width}/{self.height}"

    def display(self):
        """print in stdout"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str_(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
                .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """method that updats the attribute of a rectangle """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for idx, value in enumerate(args):
                setattr(self, attrs[idx], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ method that returns the dictionary representation of a rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
            'x': self.x, 'y': self.y}
    def to_csv(self):
        """creates a list with rectangle attribute"""
        return [self.id, self.width, self.height, self.x, self.y]
