#!/usr/bin/python3
"""defines a locked class"""


class LockedClass:
    __slots__ = ["first_name"]
    """sets an attribute"""

    def __setattr__(self, key, value):
        if not hasattr(self, key) and key != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 .format(key))
            self.__dict__[key] = value
