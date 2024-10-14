#!/usr/bin/python3
"""
This module contains a function that returns a list of
available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing the names of attributes and methods of the object.
    """
    return dir(obj)
