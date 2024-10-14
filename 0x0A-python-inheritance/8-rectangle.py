#!/usr/bin/python3
from base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Parameters:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)   # Validate width
        self.__width = width                      # Set private width
        self.integer_validator("height", height) # Validate height
        self.__height = height                    # Set private height
