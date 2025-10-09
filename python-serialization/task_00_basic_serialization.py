#!/usr/bin/python3
"""
task_00_basic_serialization.py
This module provides basic serialization and deserialization functions
for Python dictionaries using JSON files.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The output JSON file name. Existing files will be overwritten.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file into a Python dictionary.

    Args:
        filename (str): The input JSON file name.

    Returns:
        dict: The Python dictionary deserialized from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
