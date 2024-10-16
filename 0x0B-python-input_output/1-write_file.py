#!/usr/bin/python3
"""Writes string as a text file."""


def write_file(filename="", text=""):
    """Writes string as text and returns
    the number of characters written"""

    with open(filename, 'w+') as f:
        return f.write(text)
