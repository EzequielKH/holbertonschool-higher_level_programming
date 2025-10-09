#!/usr/bin/python3
"""
Module 0-read_file
This module provides a function to read and display
the contents of a text file (UTF-8 encoded).
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The path to the text file to read.

    Description:
        - Opens the file using a 'with' statement to ensure it is properly closed.
        - Reads the entire content of the file.
        - Prints the content directly to standard output without adding extra newlines.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end='')
