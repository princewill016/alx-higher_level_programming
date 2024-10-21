#!/usr/bin/python3
"""
This module contains the Base class which serves as the foundation for all other classes in the project.
It manages the id attribute to avoid code duplication and maintain consistency across derived classes.
"""


class Base:
    """
    Base class for all other classes in the project.
    
    Attributes:
        __nb_objects (int): Private class attribute to keep track of number of objects
        id (int): Public instance attribute for identification
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.
        
        Args:
            id (int, optional): Identifier for the instance. Defaults to None.
                              If None, __nb_objects is incremented and used as id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
