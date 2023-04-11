#!/usr/bin/python3
"""defines a class"""


class student:
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

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
