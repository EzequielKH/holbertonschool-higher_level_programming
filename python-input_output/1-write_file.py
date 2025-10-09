#!/usr/bin/python3
"""
Module 1-write_file
This module provides a function that writes a string to a text file (UTF-8)
and returns the number of characters written.
"""


def writefile(filename="", text=""):
    """
    Writes a string to a text file (UTF-8)
    and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string content to write into the file.

    Returns:
        int: The number of characters written to the file.

    Description:
        - Opens the file in write mode ('w'), overwriting existing content.
        - Creates the file if it does not exist.
        - Uses UTF-8 encoding for compatibility.
    """
    with open(filename, "w", encoding="utf-8") as f:
        num_chars_written = f.write(text)
    return num_chars_written
