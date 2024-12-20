#!/usr/bin/python3
"""Module 9-student.
Creates a Student class.
"""


class Student:
    """Class that defines a student by public instance.
    attributes: first_name, last_name, age.
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation
        of a Student instance.
        Returns: the dict representation of the instance.
        """

        return self.__dict__
