#!/usr/bin/python3
"""Unit tests for Base class's create method"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseCreate(unittest.TestCase):
    """Test cases for the create method in Base class"""

    def setUp(self):
        """Reset __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_create_rectangle(self):
        """Test create method with Rectangle"""
        # Test with all attributes
        r1_dictionary = {
            'width': 3,
            'height': 5,
            'x': 1,
            'y': 2,
            'id': 89
        }
        r1 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 89)
        
        # Test with minimal attributes
        r2_dictionary = {
            'width': 1,
            'height': 2
        }
        r2 = Rectangle.create(**r2_dictionary)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 0)  # Default value
        self.assertEqual(r2.y, 0)  # Default value
        self.assertEqual(r2.id, 1)  # Auto-generated ID
        
        # Test with some attributes
        r3_dictionary = {
            'width': 3,
            'height': 5,
            'id': 90
        }
        r3 = Rectangle.create(**r3_dictionary)
        self.assertEqual(r3.width, 3)
        self.assertEqual(r3.height, 5)
        self.assertEqual(r3.x, 0)  # Default value
        self.assertEqual(r3.y, 0)  # Default value
        self.assertEqual(r3.id, 90)

    def test_create_square(self):
        """Test create method with Square"""
        # Test with all attributes
        s1_dictionary = {
            'size': 3,
            'x': 1,
            'y': 2,
            'id': 89
        }
        s1 = Square.create(**s1_dictionary)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 89)
        
        # Test with minimal attributes
        s2_dictionary = {
            'size': 1
        }
        s2 = Square.create(**s2_dictionary)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 0)  # Default value
        self.assertEqual(s2.y, 0)  # Default value
        self.assertEqual(s2.id, 1)  # Auto-generated ID
        
        # Test with some attributes
        s3_dictionary = {
            'size': 3,
            'id': 90
        }
        s3 = Square.create(**s3_dictionary)
        self.assertEqual(s3.size, 3)
        self.assertEqual(s3.x, 0)  # Default value
        self.assertEqual(s3.y, 0)  # Default value
        self.assertEqual(s3.id, 90)

    def test_create_invalid(self):
        """Test create method with invalid inputs"""
        # Test with empty dictionary
        r = Rectangle.create(**{})
        self.assertEqual(r.width, 1)  # Default dummy values
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

        # Test with invalid class
        base = Base()
        result = Base.create(**{'id': 1})
        self.assertIsNone(result)

    def test_create_with_invalid_attributes(self):
        """Test create method with invalid attribute values"""
        # Test Rectangle with invalid width
        with self.assertRaises(ValueError):
            Rectangle.create(**{'width': -1})

        # Test Rectangle with invalid height
        with self.assertRaises(ValueError):
            Rectangle.create(**{'height': 0})

        # Test Square with invalid size
        with self.assertRaises(ValueError):
            Square.create(**{'size': -5})

        # Test with invalid x coordinate
        with self.assertRaises(ValueError):
            Rectangle.create(**{'width': 1, 'height': 1, 'x': -1})

        # Test with invalid y coordinate
        with self.assertRaises(ValueError):
            Square.create(**{'size': 1, 'y': -1})


if __name__ == '__main__':
    unittest.main()
