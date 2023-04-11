#!/usr/bin/python3
"""defines a class"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """initializes a new student
        Args:
        first_name(str) = the students first name
        last_name(str) = the students last name
        age(int) = the student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all the student attribute.
        Args:
            json (dict): pair to replace the attribute
            """
        for k, v in json.items():
            setattr(self, k, v)
