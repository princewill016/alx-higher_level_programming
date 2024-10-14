#!/usr/bin/python3
from rectangle import Rectangle  # Assuming rectangle.py is in the same directory

class Square(Rectangle):
    """
    A class that represents a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Parameters:
        size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)  # Validate size
        self.__size = size
        super().__init__(size, size)  # Call the Rectangle constructor

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
        str: Description of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"

    def print(self):
        """
        Prints the square representation.
        """
        print(self.__str__())
