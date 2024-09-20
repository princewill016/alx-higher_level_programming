#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """Return a new matrix with each value squared."""
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
