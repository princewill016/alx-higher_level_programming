#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
from models.rectangle import Rectangle


class TestRectangleDictionary(unittest.TestCase):
    """Test cases for Rectangle's to_dictionary method"""

    def setUp(self):
        """Reset the private class attribute between tests"""
        Rectangle._Base__nb_objects = 0

    def test_to_dictionary_basic(self):
        """Test basic dictionary representation"""
        r = Rectangle(10, 20, 1, 2, 3)
        expected = {'id': 3, 'width': 10, 'height': 20, 'x': 1, 'y': 2}
        self.assertEqual(r.to_dictionary(), expected)

    def test_to_dictionary_default_values(self):
        """Test dictionary with default x, y values"""
        r = Rectangle(10, 20)
        expected = {'id': 1, 'width': 10, 'height': 20, 'x': 0, 'y': 0}
        self.assertEqual(r.to_dictionary(), expected)

    def test_to_dictionary_no_id(self):
        """Test dictionary when id is not provided"""
        r = Rectangle(10, 20, 1, 2)
        result = r.to_dictionary()
        self.assertEqual(result['width'], 10)
        self.assertEqual(result['height'], 20)
        self.assertEqual(result['x'], 1)
        self.assertEqual(result['y'], 2)
        self.assertEqual(result['id'], 1)

    def test_to_dictionary_update(self):
        """Test using dictionary with update method"""
        r1 = Rectangle(10, 20, 1, 2, 3)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())
        self.assertFalse(r1 is r2)

    def test_to_dictionary_modified_values(self):
        """Test dictionary after modifying attributes"""
        r = Rectangle(10, 20, 1, 2, 3)
        original_dict = r.to_dictionary()
        r.width = 30
        r.height = 40
        r.x = 3
        r.y = 4
        modified_dict = r.to_dictionary()
        self.assertNotEqual(original_dict, modified_dict)
        self.assertEqual(modified_dict['width'], 30)
        self.assertEqual(modified_dict['height'], 40)
        self.assertEqual(modified_dict['x'], 3)
        self.assertEqual(modified_dict['y'], 4)


if __name__ == '__main__':
    unittest.main()
