#!/usr/bin/python3
import sys
from os.path import exists
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"
items = load_from_json_file(filename) if exists(filename) else []

for arg in sys.argv[1:]:
    items.append(arg)

save_to_json_file(items, filename)