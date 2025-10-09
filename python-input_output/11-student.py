#!/usr/bin/python3
"""
Module that defines a Student class with JSON serialization
and deserialization capabilities.
"""

class Student:
    """
    Represents a student with first name, last name, and age.

    Attributes:
        first_name (str): First name of the student.
        last_name (str): Last name of the student.
        age (int): Age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        If `attrs` is a list of attribute names, only those attributes
        will be included. Otherwise, all attributes are included.

        Args:
            attrs (list, optional): List of attribute names to include.

        Returns:
            dict: Dictionary of the requested attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            filtered_dict = {}
            for attr_name in attrs:
                if hasattr(self, attr_name):
                    filtered_dict[attr_name] = getattr(self, attr_name)
            return filtered_dict

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with
        values from a JSON dictionary.

        Args:
            json (dict): Dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
