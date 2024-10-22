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

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation.
        
        Args:
            json_string (str): A string representing a list of dictionaries
        
        Returns:
            list: The list of dictionaries represented by json_string.
                Returns an empty list if json_string is None or empty.
                Otherwise returns the list represented by json_string.
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.
        
        Args:
            list_objs (list): A list of instances who inherits from Base
        
        Notes:
            - The filename will be <Class name>.json (e.g., Rectangle.json)
            - If list_objs is None, an empty list will be saved
            - The file will be overwritten if it already exists
        """
        filename = cls.__name__ + ".json"
        
        if list_objs is None:
            list_objs = []
        
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set.
        
        Args:
            **dictionary: Double pointer to a dictionary of attributes
        
        Returns:
            instance: An instance with all attributes already set
            
        Notes:
            - Creates a "dummy" instance with mandatory attributes
            - Updates the dummy instance with real values using update method
            - Uses **dictionary as **kwargs for the update method
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create dummy Rectangle with width=1, height=1
        elif cls.__name__ == "Square":
            dummy = cls(1)     # Create dummy Square with size=1
        else:
            return None
        
        dummy.update(**dictionary)  # Update dummy instance with real values
        return dummy
