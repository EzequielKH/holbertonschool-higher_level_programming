#!/usr/bin/python3
"""Define a class Square with a private instance attribute size."""


class Square:
    """Represents a square with a private size."""

    def __init__(self, size):
        """Initialize the square with the given size.

        Args:
            size (any): The size of the square (no type/value checks here).
        """
        self.__size = size
