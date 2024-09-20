#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Return the key with the biggest integer value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary with integer values.

    Returns:
        str: The key with the highest value, or None if the dictionary is empty.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
