#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replace or add a key/value pair in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key, always a string.
        value: The value, can be any type.

    Returns:
        None
    """
    a_dictionary[key] = value
