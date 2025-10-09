#!/usr/bin/python3
"""
Module that defines a function for serializing an object to a JSON-compatible dictionary.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures
    (list, dictionary, string, integer, and boolean)
    for JSON serialization of an object.

    Args:
        obj (object): Instance of a class.

    Returns:
        dict: A dictionary containing the serializable attributes of the object.
    """
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
