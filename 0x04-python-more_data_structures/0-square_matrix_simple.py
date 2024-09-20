#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Compute the square value of all integers in a matrix.

    Args:
        matrix (list): A 2-dimensional list of integers.

    Returns:
        list: A new matrix of the same size, with each value squared.
    """
    return [[x ** 2 for x in row] for row in matrix]
