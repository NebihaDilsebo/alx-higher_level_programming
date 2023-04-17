#!/usr/bin/python3
"represents a class base"""


class Base:
    """creates a private  class attribute base"""

    __nb_objects = 0
    """initializes id"""

    def __init__(self, id=None):
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
