#!/usr/bin/python3
"""
Module that defines a Student class.
"""


class Student:

    """
    A class that represents a student.
    Attributes:
    first_name (str): The first name of the student.
    last_name (str): The last name of the student.
    age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.
        Args:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Return a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
