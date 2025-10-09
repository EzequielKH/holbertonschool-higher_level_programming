#!/usr/bin/python3
"""
Module 5-save_to_json_file
This module provides a function to write a Python object to a file
as a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj (any): The Python object to serialize and write to the file.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
