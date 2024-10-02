#!/usr/bin/python3
"""
This module defines a Square class.
The class represents a geometric square with size and position attributes,
and methods to calculate area and print the square.
"""


class Square:
    """
    A class that defines a square.
    
    This class represents a square with size and position attributes.
    It provides methods to calculate area and print the square using '#' characters.

    Attributes:
        __size (int): The size of the square's sides.
        __position (tuple): The position of the square as a tuple of 2 positive integers.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square's sides. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square's sides.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The position as a tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters.
        
        If size is 0, prints an empty line.
        Uses position for spacing before printing the square.
        """
        if self.__size == 0:
            print()
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print the square with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        result = []
        if self.__size == 0:
            return "\n"

        # Add vertical offset
        for _ in range(self.__position[1]):
            result.append("")

        # Add the square with horizontal offset
        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(result)
