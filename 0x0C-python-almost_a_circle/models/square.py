#!/usr/bin/python3
"""module that inherits from Base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes an instance of square class"""
        super().__init__(size, size, x, y, id)


    @property
    def size(self):
        """Returns the width of square instance"""
        return self.__width

    @size.setter
    def size(self, value):
        """sets the size of the square instance"""
        self.width = value
        self.height = value

    def __str_(self):
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)


        
    def update(self, *args, **kwargs):
            """method that updats the attribute of a Square"""
            if args:
                attrs = ["id", "width", "height", "x", "y"]
                for idx, value in enumerate(args):
                    setattr(self, attrs[idx], value)
            elif kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
            """ method that returns the dictionary representation of a Square"""
            return {'id': self.d, 'width':self.width, 'height': self.height, 'x': self.x, 'y':self.y}
