#!/usr/bin/python3
"""
This module contains a function to return a Python object represented by a JSON string.
"""

import json

def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): A JSON string representation of an object.

    Returns:
        object: A Python data structure (dict, list, str, int, float, bool, or None).
    """
    return json.loads(my_str)
