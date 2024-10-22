#!/usr/bin/python3
"""
Unit tests for the Base class.
Tests the functionality of the Base class including JSON string conversion.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    Tests initialization and JSON string conversion functionality.
    """

    def setUp(self):
        """Reset Base.__nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_to_json_string_none(self):
        """Test conversion of None to JSON string"""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_empty_list(self):
        """Test conversion of empty list to JSON string"""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_single_dict(self):
        """Test conversion of list with single dictionary to JSON string"""
        dictionary = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        json_string = Base.to_json_string([dictionary])
        expected = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(json_string, expected)

    def test_to_json_string_multiple_dicts(self):
        """Test conversion of list with multiple dictionaries to JSON string"""
        dictionaries = [
            {'id': 1, 'width': 10, 'height': 7},
            {'id': 2, 'width': 2, 'height': 4}
        ]
        json_string = Base.to_json_string(dictionaries)
        expected = '[{"id": 1, "width": 10, "height": 7}, {"id": 2, "width": 2, "height": 4}]'
        self.assertEqual(json_string, expected)

    def test_to_json_string_nested_dict(self):
        """Test conversion of list with nested dictionary to JSON string"""
        dictionary = {'id': 1, 'nested': {'key': 'value'}}
        json_string = Base.to_json_string([dictionary])
        expected = '[{"id": 1, "nested": {"key": "value"}}]'
        self.assertEqual(json_string, expected)


if __name__ == '__main__':
    unittest.main()
