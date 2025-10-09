#!/usr/bin/python3
"""
Module that defines a function to generate Pascal's Triangle.
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle of size `n`.

    Each element in the triangle is the sum of the two elements
    above it. The triangle is represented as a list of lists of integers.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
