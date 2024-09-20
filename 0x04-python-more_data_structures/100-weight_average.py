#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Return the weighted average of all integers in a list of tuples.

    Args:
        my_list (list): A list of tuples containing (<score>, <weight>).

    Returns:
        float: The weighted average, or 0 if the list is empty.
    """
    if not my_list:
        return 0

    total_score = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    return total_score / total_weight if total_weight else 0
