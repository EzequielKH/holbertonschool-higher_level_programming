#!/usr/bin/python3
"""
This module defines a function that prints text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> text_indentation("Hello. How are you? Fine: thanks.")
        Hello.
        <BLANKLINE>
        How are you?
        <BLANKLINE>
        Fine:
        <BLANKLINE>
        thanks.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    start = 0
    for i, char in enumerate(text):
        if char in ".?:":
            line = text[start:i + 1].strip()
            print(line, end="\n\n")
            start = i + 1
    if start < len(text):
        line = text[start:].strip()
        if line:
            print(line, end="")
