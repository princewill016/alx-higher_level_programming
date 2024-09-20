#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Delete a key in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to delete.

    Returns:
        None
    """
    a_dictionary.pop(key, None)
