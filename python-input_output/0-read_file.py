#!/usr/bin/python3


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end='')
