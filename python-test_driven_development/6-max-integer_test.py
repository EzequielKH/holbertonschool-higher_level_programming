#!/usr/bin/python3
"""Unittest for max_integer([..])
This module contains unittests for the function max_integer.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when the max value is at the beginning"""
        self.assertEqual(max_integer([10, 2, 3, 1]), 10)

    def test_max_in_middle(self):
        """Test when the max value is in the middle"""
        self.assertEqual(max_integer([1, 5, 4, 3]), 5)

    def test_single_element_list(self):
        """Test with a single-element list"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list (should return None)"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test a list containing negative numbers"""
        self.assertEqual(max_integer([-3, -1, -7, -2]), -1)

    def test_mixed_numbers(self):
        """Test a list containing both positive and negative numbers"""
        self.assertEqual(max_integer([-10, -5, 0, 5, 10]), 10)

    def test_all_equal_numbers(self):
        """Test a list where all numbers are the same"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_float_numbers(self):
        """Test a list containing floats"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 2.9]), 3.3)

    def test_mixed_ints_and_floats(self):
        """Test a list containing both ints and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 2.9]), 3)

    def test_large_numbers(self):
        """Test a list with very large numbers"""
        self.assertEqual(max_integer([9999999999, 10000000000, 9999999998]), 10000000000)


if __name__ == '__main__':
    unittest.main()
