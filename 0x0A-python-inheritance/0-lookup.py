#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    obj: The object to inspect.

    Returns:
    list: A list of attributes and methods of the object.
    """
    return dir(obj)
