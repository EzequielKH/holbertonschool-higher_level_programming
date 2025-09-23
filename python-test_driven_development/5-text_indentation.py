#!/usr/bin/python3
"""Text indentation module."""

def text_indentation(text):
    """Print text with 2 new lines after each '.', '?', or ':'.

    :param text: string to print
    :raises TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    start = 0
    length = len(text)

    for i, char in enumerate(text):
        if char in separators:
            print(text[start:i + 1].strip())
            print()
            start = i + 1

    if start < length:
        print(text[start:].strip())
