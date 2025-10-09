#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, then saves them to a JSON file.
"""

import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_items_and_save_to_json():
    """Add command-line arguments to add_item.json as a JSON list."""
    filename = "add_item.json"
    items = load_from_json_file(filename) if os.path.exists(filename) else []

    for arg in sys.argv[1:]:
        items.append(arg)

    save_to_json_file(items, filename)

if __name__ == "__main__":
    add_items_and_save_to_json()
