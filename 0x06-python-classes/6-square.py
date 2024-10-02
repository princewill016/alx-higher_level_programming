#!/usr/bin/python3
"""
Module that defines a Square class.
"""


class Square:
    """
    Class that defines a square by its size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position to start printing the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): The position to set for the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                isinstance(value[0], int) and isinstance(value[1], int) and
                value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character # to stdout, considering the position.

        If size is 0, print an empty line. The position attribute is used to
        print leading spaces and new lines before the square.
        """
        if self.__size == 0:
            print()
        else:
            # Print empty lines for the vertical position
            for _ in range(self.__position[1]):
                print()
            # Print the square with leading spaces for horizontal position
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
