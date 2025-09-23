#!/usr/bin/python3
def matrix_divided(matrix, div):

    """
    This module provides a function to divide all elements of a matrix.
    """

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix: list of lists of integers/floats.
        div: number (int or float).

    Returns:
        A new matrix with elements divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: if matrix is not a list of lists of numbers,
                   or if rows are not the same size,
                   or if div is not a number.
        ZeroDivisionError: if div is 0.
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if matrix and not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
