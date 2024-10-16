#!/usr/bin/python3
"""  reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """ function to read and print the content
    of a UTF-8 encoded text file."""
    with open(filename) as f:
        print(f.read(), end="")
