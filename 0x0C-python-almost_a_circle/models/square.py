#!/usr/bin/python3
"""
This module contains the Square class which inherits from Rectangle.
It defines a square by its size and position (x, y).
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    Represents a square with size and position attributes.

    Attributes:
        size (int): Size of the square (both width and height)
        x (int): X-coordinate of the square's position
        y (int): Y-coordinate of the square's position
        id (int): Identifier of the square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): Size of the square
            x (int, optional): X-coordinate of the square. Defaults to 0.
            y (int, optional): Y-coordinate of the square. Defaults to 0.
            id (int, optional): Identifier of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return string representation of Square instance.

        Returns:
            str: String in the format [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size attribute.
        Sets both width and height to the same value.

        Args:
            value (int): Size value to set

        Note:
            The value validation is handled by the Rectangle class
            width and height setters.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square attributes.
        
        Args:
            *args: Variable length argument list.
                1st argument represents id attribute
                2nd argument represents size attribute
                3rd argument represents x attribute
                4th argument represents y attribute
            **kwargs: Arbitrary keyword arguments.
                Each key represents an attribute to the instance

        Note:
            **kwargs is skipped if *args exists and is not empty
        """
        if args and len(args) > 0:
            attributes = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if i < len(attributes):
                    setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of a Square.

        Returns:
            dict: Dictionary containing the Square's attributes:
                - id: identifier of the square
                - size: size of the square
                - x: x-coordinate of the square
                - y: y-coordinate of the square
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
