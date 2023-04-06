#!/usr/bin/python3
class LockedClass:
    __slots__ = ["first_name"]

    def __setattr__(self, key, value):
        if not hasattr(self, key) and key != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 .format(key))
        super().__setattr__(key, value)
