#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """Square shape, inherits from Rectangle."""

    def __init__(self, size):
        """
        Initialize a square.

        Args:
            size (int): the size of the square sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
