#!/usr/bin/python3
"""module that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """rectangle class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes an instance of Rectangle class"""
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
            raise TypeError ('width must be an integer')
        elif value <= 0:
            raise ValueError ('width must be > 0')
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
            self.__height =value

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
        """updates by overriding"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
