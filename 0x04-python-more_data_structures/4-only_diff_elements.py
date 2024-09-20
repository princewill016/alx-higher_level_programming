#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Return a set of elements present in only one of the two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set of elements present in only one of the sets.
    """
    return set_1 ^ set_2
