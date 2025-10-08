#!/usr/bin/python3

import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items_and_save_to_json():
    filename = "add_item.json"
    items = []
    if os.path.exists(filename):
        items = load_from_json_file(filename)

    for arg in sys.argv[1:]:
        items.append(arg)

    save_to_json_file(items, filename)


if __name__ == "__main__":
    add_items_and_save_to_json()
