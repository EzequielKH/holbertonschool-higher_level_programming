#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix or (len(matrix) == 1 and not matrix[0]):
        print()
        return

    for row in matrix:
        for i, element in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(element), end="")
            else:
                print("{:d}".format(element), end=" ")
        print()
