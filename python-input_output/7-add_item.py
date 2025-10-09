#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list
and saves them to a file in JSON format.

- The list is saved to a file named "add_item.json".
- If the file does not exist, it is created.
- Uses the functions:
    save_to_json_file() → from 5-save_to_json_file.py
    load_from_json_file() → from 6-load_from_json_file.py
"""
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items_and_save_to_json():
    """
    Adds all command-line arguments to a list and saves it as JSON.

    - Loads the existing list from 'add_item.json' if it exists.
    - Appends new arguments passed via the command line.
    - Saves the updated list back to 'add_item.json'.
    """

    filename = "add_item.json"
    items = []
    if os.path.exists(filename):
        items = load_from_json_file(filename)

    for arg in sys.argv[1:]:
        items.append(arg)

    save_to_json_file(items, filename)


if __name__ == "__main__":
    add_items_and_save_to_json()
