#!/usr/bin/python3
"""
Module that defines a function to append text to a file.
"""


def append_write(filename="", text=""):

    """
    Appends a string at the end of a text file (UTF8) and returns
    the number of characters added.

    Args:
        filename (str): The name of the file to append text to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        num_characters_added = f.write(text)
    return num_characters_added
