#!/usr/bin/python3

def read_file(filename=""):
    """ defines a function to read and print the content
    of a UTF-8 encoded text file."""
    with open(filename, "r") as files:
        print(files.read(), end="")
