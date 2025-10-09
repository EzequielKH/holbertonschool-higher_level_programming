 #!/usr/bin/python3
"""
task_01_pickle.py
This module defines a CustomObject class with serialization and
deserialization capabilities using the pickle module.
"""

import pickle


class CustomObject:
    """A class representing a custom object with serialization support."""

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Whether the object represents a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes of the object in a formatted way."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object to a file using pickle.

        Args:
            filename (str): The file path to save the serialized object.

        Returns:
            None
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject from a pickle file.

        Args:
            filename (str): The file path containing the serialized object.

        Returns:
            CustomObject: The deserialized object, or None if deserialization fails.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            return obj
        except Exception:
            return None
