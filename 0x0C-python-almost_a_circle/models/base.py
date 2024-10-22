#!/usr/bin/python3
"""
This module contains the Base class which serves as the foundation for all other classes in the project.
It manages the id attribute to avoid code duplication and maintain consistency across derived classes.
"""
import json
import os
import csv

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
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create dummy Rectangle with width=1, height=1
        elif cls.__name__ == "Square":
            dummy = cls(1)     # Create dummy Square with size=1
        else:
            return None
        
        dummy.update(**dictionary)  # Update dummy instance with real values
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Create a list of instances from a JSON file.
        
        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".json"
        
        if not os.path.exists(filename):
            return []
        
        with open(filename, 'r', encoding='utf-8') as f:
            json_string = f.read()
        
        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize instances to a CSV file.
        
        Args:
            list_objs (list): A list of instances who inherits from Base
            
        Notes:
            - The filename will be <Class name>.csv
            - Format for Rectangle: <id>,<width>,<height>,<x>,<y>
            - Format for Square: <id>,<size>,<x>,<y>
        """
        filename = cls.__name__ + ".csv"
        
        if list_objs is None:
            list_objs = []

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize instances from a CSV file.
        
        Returns:
            list: A list of instances
            
        Notes:
            - The filename will be <Class name>.csv
            - Returns an empty list if the file doesn't exist
            - Format for Rectangle: <id>,<width>,<height>,<x>,<y>
            - Format for Square: <id>,<size>,<x>,<y>
        """
        filename = cls.__name__ + ".csv"
        
        if not os.path.exists(filename):
            return []

        instances = []
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # Convert all values to integers
                row = [int(x) for x in row]
                
                if cls.__name__ == "Rectangle":
                    dictionary = {
                        'id': row[0],
                        'width': row[1],
                        'height': row[2],
                        'x': row[3],
                        'y': row[4]
                    }
                elif cls.__name__ == "Square":
                    dictionary = {
                        'id': row[0],
                        'size': row[1],
                        'x': row[2],
                        'y': row[3]
                    }
                
                instance = cls.create(**dictionary)
                instances.append(instance)
                
        return instances
