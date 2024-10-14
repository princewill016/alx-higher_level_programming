#!/usr/bin/python3
"""
This module contains the MyList class, which inherits from list.
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    This class adds a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        This method does not modify the original list.
        It creates a new sorted list and prints it.
        """
        print(sorted(self))
