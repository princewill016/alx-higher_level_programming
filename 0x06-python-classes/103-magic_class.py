#!/usr/bin/python3
"""
This module defines a MagicClass that performs calculations for a circle.
The implementation matches specific Python bytecode instructions.
"""


import math


class MagicClass:
    """
    A class that represents a circle and performs geometric calculations.
    This implementation matches specific bytecode instructions.
    """
    def __init__(self, radius=0):
        """
        Initialize the MagicClass.

        Args:
            radius (int or float, optional): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If radius is not a number (int or float).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
