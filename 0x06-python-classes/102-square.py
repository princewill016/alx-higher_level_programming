#!/usr/bin/python3
"""
This module defines a Square class.
The class represents a geometric square that can be compared with other squares
based on their areas.
"""


class Square:
    """
    A class that defines a square with comparison capabilities.
    
    This class represents a square that can be compared with other squares
    based on their areas. It supports all standard comparison operators.

    Attributes:
        __size (float or int): The size of the square's sides.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (float or int, optional): The size of the square's sides. Defaults to 0.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            float or int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (float or int): The size of the square's sides.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            float or int: The area of the square (size * size).
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equal comparison based on area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparison based on area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison based on area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison based on area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less than comparison based on area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison based on area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()
