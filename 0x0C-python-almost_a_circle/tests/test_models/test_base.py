#!/usr/bin/python3
"""
Unit tests for the Base class.
Tests the functionality of the Base class including from_json_string method.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseFromJsonString(unittest.TestCase):
    """
    Test cases for the Base class from_json_string method.
    """

    def test_from_json_string_none(self):
        """Test conversion of None to list"""
        list_output = Base.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_from_json_string_empty_string(self):
        """Test conversion of empty string to list"""
        list_output = Base.from_json_string("")
        self.assertEqual(list_output, [])

    def test_from_json_string_empty_list(self):
        """Test conversion of JSON string representing empty list"""
        list_output = Base.from_json_string("[]")
        self.assertEqual(list_output, [])

    def test_from_json_string_single_dict(self):
        """Test conversion of JSON string with single dictionary"""
        json_input = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        list_output = Base.from_json_string(json_input)
        expected = [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}]
        self.assertEqual(list_output, expected)

    def test_from_json_string_multiple_dicts(self):
        """Test conversion of JSON string with multiple dictionaries"""
        json_input = '[{"id": 1, "width": 10, "height": 7}, {"id": 2, "width": 2, "height": 4}]'
        list_output = Base.from_json_string(json_input)
        expected = [
            {'id': 1, 'width': 10, 'height': 7},
            {'id': 2, 'width': 2, 'height': 4}
        ]
        self.assertEqual(list_output, expected)

    def test_from_json_string_nested_dict(self):
        """Test conversion of JSON string with nested dictionary"""
        json_input = '[{"id": 1, "nested": {"key": "value"}}]'
        list_output = Base.from_json_string(json_input)
        expected = [{'id': 1, 'nested': {'key': 'value'}}]
        self.assertEqual(list_output, expected)

    def test_from_json_string_types(self):
        """Test that method returns proper types"""
        json_input = '[{"id": 1, "width": 10, "height": 7}]'
        list_output = Base.from_json_string(json_input)
        self.assertTrue(isinstance(list_output, list))
        self.assertTrue(isinstance(list_output[0], dict))

    def test_from_json_string_invalid_json(self):
        """Test handling of invalid JSON string"""
        json_input = '[{invalid json}]'
        with self.assertRaises(json.JSONDecodeError):
            Base.from_json_string(json_input)

    def test_from_json_string_round_trip(self):
        """Test conversion from list to JSON string and back"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_string = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_string)
        self.assertEqual(list_input, list_output)


if __name__ == '__main__':
    unittest.main()
