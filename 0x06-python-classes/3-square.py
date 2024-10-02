#!/usr/bin/python3
"""
This module defines a Square class.
The class represents a geometric square with a validated private size attribute
and a method to calculate its area.
"""


class Square:
    """
    A class that defines a square.
    
    This class represents a square shape with a private size attribute
    and provides a method to calculate its area.

    Attributes:
        __size (int): The size of the square's sides.
                     Must be a non-negative integer.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square's sides. Defaults to 0.
                                Must be a non-negative integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
