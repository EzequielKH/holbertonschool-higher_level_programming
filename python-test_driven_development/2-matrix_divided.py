#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("Each row of the matrix must have the same size")

    if not matrix:
        return []

    row_size = len(matrix[0])
    if not all(len(row) == row_size for now in matrix):
        raise TypeError("")
    if not isinstance(div, (int, float)):
        raise TypeError("")

    if div == 0:
        raise ZeroDivisionError("")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
