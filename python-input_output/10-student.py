#!/usr/bin/python3
"""
Module that defines a Student class with JSON serialization.
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

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the Student instance.

        If `attrs` is a list of strings, only attributes contained in
        the list will be included. Otherwise, all attributes are included.

        Args:
            attrs (list, optional): List of attribute names to include.

        Returns:
            dict: A dictionary containing the
            requested attributes of the student.
        """
        if attrs is None:
            return self.__dict__.copy()

        filtered_dict = {}
        for attr in attrs:
            if attr in self.__dict__:
                filtered_dict[attr] = self.__dict__[attr]
        return filtered_dict
