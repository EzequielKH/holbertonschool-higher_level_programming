#!/usr/bin/python3
"""Module 5-save_to_json_file:
Writes a Python object to a text file as a JSON representation.
"""
import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.

    Args:
        my_obj: The object to serialize (list, dict, etc.).
        filename: Name of the file to write.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
