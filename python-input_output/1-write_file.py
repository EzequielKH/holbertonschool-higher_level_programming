#!/usr/bin/python3


def writefile(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as f:
        num_chars_written = f.write(text)
    return num_chars_written
