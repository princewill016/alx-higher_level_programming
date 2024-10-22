#!/usr/bin/python3
"""Unit tests for Base class's load_from_file method"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestLoadFromFile(unittest.TestCase):
    """Test cases for the load_from_file method in Base class"""

    def setUp(self):
        """Reset __nb_objects before each test and remove any existing files"""
        Base._Base__nb_objects = 0
        for filename in ['Rectangle.json', 'Square.json']:
            if os.path.exists(filename):
                os.remove(filename)

    def tearDown(self):
        """Clean up any created files after tests"""
        for filename in ['Rectangle.json', 'Square.json']:
            if os.path.exists(filename):
                os.remove(filename)

    def test_load_from_file_rectangles(self):
        """Test loading Rectangle instances from file"""
        # Create and save some rectangles
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])

        # Load rectangles from file
        list_rectangles = Rectangle.load_from_file()

        # Verify the loaded rectangles
        self.assertEqual(len(list_rectangles), 2)
        self.assertIsInstance(list_rectangles[0], Rectangle)
        self.assertIsInstance(list_rectangles[1], Rectangle)
        
        # Verify attributes of first rectangle
        self.assertEqual(list_rectangles[0].width, 10)
        self.assertEqual(list_rectangles[0].height, 7)
        self.assertEqual(list_rectangles[0].x, 2)
        self.assertEqual(list_rectangles[0].y, 8)
        self.assertEqual(list_rectangles[0].id, 1)
        
        # Verify attributes of second rectangle
        self.assertEqual(list_rectangles[1].width, 2)
        self.assertEqual(list_rectangles[1].height, 4)
        self.assertEqual(list_rectangles[1].x, 0)
        self.assertEqual(list_rectangles[1].y, 0)
        self.assertEqual(list_rectangles[1].id, 2)

    def test_load_from_file_squares(self):
        """Test loading Square instances from file"""
        # Create and save some squares
        s1 = Square(5, 1, 3, 3)
        s2 = Square(7, 0, 0, 4)
        Square.save_to_file([s1, s2])

        # Load squares from file
        list_squares = Square.load_from_file()

        # Verify the loaded squares
        self.assertEqual(len(list_squares), 2)
        self.assertIsInstance(list_squares[0], Square)
        self.assertIsInstance(list_squares[1], Square)
        
        # Verify attributes of first square
        self.assertEqual(list_squares[0].size, 5)
        self.assertEqual(list_squares[0].x, 1)
        self.assertEqual(list_squares[0].y, 3)
        self.assertEqual(list_squares[0].id, 3)
        
        # Verify attributes of second square
        self.assertEqual(list_squares[1].size, 7)
        self.assertEqual(list_squares[1].x, 0)
        self.assertEqual(list_squares[1].y, 0)
        self.assertEqual(list_squares[1].id, 4)

    def test_load_from_nonexistent_file(self):
        """Test loading from a file that doesn't exist"""
        list_rectangles = Rectangle.load_from_file()
        self.assertEqual(list_rectangles, [])

    def test_load_from_empty_file(self):
        """Test loading from an empty file"""
        # Create empty file
        with open('Rectangle.json', 'w') as f:
            f.write('[]')
        
        list_rectangles = Rectangle.load_from_file()
        self.assertEqual(list_rectangles, [])

    def test_load_from_corrupted_file(self):
        """Test loading from a corrupted JSON file"""
        # Create corrupted JSON file
        with open('Rectangle.json', 'w') as f:
            f.write('{invalid json')
        
        with self.assertRaises(json.decoder.JSONDecodeError):
            Rectangle.load_from_file()


if __name__ == '__main__':
    unittest.main()
