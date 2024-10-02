#!/usr/bin/python3

"""
This module defines a Square class.
The class represents a geometric square with a private size attribute.
"""


class Square:

    """
    A class that defines a square.
    
    This class represents a square shape with a private size attribute.
    The size is set at instantiation without type or value verification.

    Attributes:
        __size (int): The size of the square's sides.
    """
    def __init__(self, size):

        """
        Initializes a new Square instance.

        Args:
            size: The size of the square's sides.
                 No type/value verification is performed.
        """
        self.__size = size
