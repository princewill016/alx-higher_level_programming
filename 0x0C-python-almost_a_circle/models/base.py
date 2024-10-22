#!/usr/bin/python3
"""
This module contains the Base class which serves as the foundation for all other classes in the project.
It manages the id attribute to avoid code duplication and maintain consistency across derived classes.
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.
        
        Args:
            list_dictionaries (list): A list of dictionaries to convert to JSON string
        
        Returns:
            str: The JSON string representation of list_dictionaries.
                Returns "[]" if list_dictionaries is None or empty.
                Otherwise returns the JSON string representation.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
