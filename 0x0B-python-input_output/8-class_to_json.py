#!/usr/bin/python3
""" Returns the dictionary description with
simple data structure (list, dictionary,
string, integer and boolean)
for JSON serialization of an object.
"""


def class_to_json(obj):
    """Creates a dict description of obj."""

    return obj.__dict__
