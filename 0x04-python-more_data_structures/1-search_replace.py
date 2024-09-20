#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replace all occurrences of an element in a list with another element.

    Args:
        my_list (list): The initial list.
        search: The element to search for in the list.
        replace: The element to replace the searched element with.

    Returns:
        list: A new list with the elements replaced.
    """
    return [replace if x == search else x for x in my_list]
