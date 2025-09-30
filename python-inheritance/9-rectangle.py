#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """Rectangle shape, inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize a rectangle.

        Args:
            width (int): rectangle width.
            height (int): rectangle height.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return rectangle description in the format:
        [Rectangle] <width>/<height>"""
        return f"[Rectangle] {self.__width}/{self.__height}"
