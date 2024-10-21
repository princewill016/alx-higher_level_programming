#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from Base
"""


class Rectangle:
    """
    Rectangle class that defines a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance
        
        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int, optional): x coordinate of rectangle. Defaults to 0.
            y (int, optional): y coordinate of rectangle. Defaults to 0.
            id (int, optional): Instance identifier. Defaults to None.
        """
        super().__init__()
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

    def __str__(self):
        """
        Returns string representation of Rectangle instance
        
        Returns:
            str: String in format [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
