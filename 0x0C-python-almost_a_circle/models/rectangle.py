#!/usr/bin/python3
"""
This module contains the Rectangle class which inherits from Base.
It defines a rectangle by its width, height, and position (x, y).
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.
    Represents a rectangle with width, height, and position attributes.

    Attributes:
        width (int): Width of the rectangle
        height (int): Height of the rectangle
        x (int): X-coordinate of the rectangle's position
        y (int): Y-coordinate of the rectangle's position
        id (int): Identifier of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int, optional): X-coordinate of the rectangle. Defaults to 0.
            y (int, optional): Y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): Identifier of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute

        Args:
            value (int): Width value to set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute

        Args:
            value (int): Height value to set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x attribute

        Args:
            value (int): X-coordinate value to set
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y attribute

        Args:
            value (int): Y-coordinate value to set
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
