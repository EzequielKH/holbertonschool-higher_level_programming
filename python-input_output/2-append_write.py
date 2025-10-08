#!/usr/bin/python3


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as f:
        num_characters_added = f.write(text)
    return num_characters_added
