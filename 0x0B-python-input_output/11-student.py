#!/usr/bin/python3
"""
This module defines a class Student.
"""

class Student:
    """
    Defines a student with first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.
        If attrs is a list of strings, only the attribute names in this
        list will be included in the dictionary.
        Args:
            attrs (list): List of strings representing attribute names.
        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        Args:
            json (dict): A dictionary where keys are attribute names and values are attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
