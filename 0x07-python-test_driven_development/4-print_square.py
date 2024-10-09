#!/usr/bin/python3
"""
This module provides a function that prints a square with #.
"""


def print_square(size):
    """
    Print a square with the character #.
    Args:
        size: length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        print("#" * size)
