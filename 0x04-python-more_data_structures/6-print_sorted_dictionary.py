#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Print a dictionary by ordered keys.

    Args:
        a_dictionary (dict): The dictionary to print.
    """
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
