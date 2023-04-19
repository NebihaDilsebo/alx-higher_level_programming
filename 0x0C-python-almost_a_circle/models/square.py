#!/usr/bin/python3
"""module that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes an instance of Square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.heigt = value

    def __str__(self):
        """updates by overriding"""
        return "[square] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                    self.y,
                                                    self.width,
                                                    self.height)

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
        """returns the dictionary representation of a rectangle"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
