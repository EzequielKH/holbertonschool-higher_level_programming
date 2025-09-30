#!/usr/bin/python3
"""Defines a lookup class."""


def lookup(obj):

    """
    Returns a list of available attributes and methods of an object,
    excluding common dunder methods.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings, where each string is the name of an attribute or method.
    """
    all_members = dir(obj)
    filtered_members = [
        member for member in all_members 
        if not (member.startswith('__') and member.endswith('__') and len(member) > 4)
    ]
    return filtered_members
