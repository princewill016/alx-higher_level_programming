#!/usr/bin/python3
"""
Module that defines a Square class.
"""


class Square:
    """
    Class that defines a square by its size.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.size = size  # Use the setter to validate size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The size to set for the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
       

