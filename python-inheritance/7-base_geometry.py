#!/usr/bin/python3
"""Defines a base geometry class with tests."""


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Raise an exception because area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is a positive integer.

        Args:
            name (str): always a string representing the name.
            value (int): the value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


import unittest


class TestBaseGeometry(unittest.TestCase):
    """Unit tests for the BaseGeometry class."""

    def setUp(self):
        """Create an instance of BaseGeometry for testing."""
        self.bg = BaseGeometry()

    def test_area_not_implemented(self):
        """area() should raise an Exception."""
        with self.assertRaises(Exception) as e:
            self.bg.area()
        self.assertEqual(str(e.exception), "area() is not implemented")

    def test_integer_validator_valid(self):
        """integer_validator should pass for valid positive integers."""
        try:
            self.bg.integer_validator("width", 10)
            self.bg.integer_validator("height", 5)
        except Exception as e:
            self.fail(f"integer_validator raised {type(e).__name__} unexpectedly!")

    def test_integer_validator_not_integer(self):
        """integer_validator should raise TypeError for non-integers."""
        with self.assertRaises(TypeError) as e:
            self.bg.integer_validator("width", "10")
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            self.bg.integer_validator("height", 5.5)
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_integer_validator_zero_or_negative(self):
        """integer_validator should raise ValueError for <= 0."""
        with self.assertRaises(ValueError) as e:
            self.bg.integer_validator("width", 0)
        self.assertEqual(str(e.exception), "width must be greater than 0")

        with self.assertRaises(ValueError) as e:
            self.bg.integer_validator("height", -3)
        self.assertEqual(str(e.exception), "height must be greater than 0")


if __name__ == "__main__":
    unittest.main()
