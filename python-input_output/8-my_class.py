#!/usr/bin/python3
"""
Module that defines the MyClass class.
"""


class MyClass:
    """
    A simple class example with a name and a number attribute.

    Attributes:
        name (str): The name of the instance.
        number (int): A numerical attribute initialized to 0.
    """

    def __init__(self, name):
        """
        Initialize a new MyClass instance.

        Args:
            name (str): The name of the instance.
        """
        self.name = name
        self.number = 0

    def __str__(self):
        """
        Return a human-readable string
        representation of the instance.

        Format: [MyClass] <name> - <number>

        Returns:
            str: The formatted string representing the instance.
        """
        return "[MyClass] {} - {:d}".format(self.name, self.number)
