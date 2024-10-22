#!/usr/bin/python3
"""Unit tests for Base class's CSV serialization methods"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestCSVMethods(unittest.TestCase):
    """Test cases for the CSV serialization methods in Base class"""

    def setUp(self):
        """Reset __nb_objects before each test and remove any existing files"""
        Base._Base__nb_objects = 0
        for filename in ['Rectangle.csv', 'Square.csv']:
            if os.path.exists(filename):
                os.remove(filename)

    def tearDown(self):
        """Clean up any created files after tests"""
        for filename in ['Rectangle.csv', 'Square.csv']:
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_to_file_csv_rectangles(self):
        """Test saving Rectangle instances to CSV file"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file_csv([r1, r2])

        # Verify file exists
        self.assertTrue(os.path.exists('Rectangle.csv'))

        # Verify file contents
        with open('Rectangle.csv', 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 2)
            self.assertEqual(lines[0].strip(), '1,10,7,2,8')
            self.assertEqual(lines[1].strip(), '2,2,4,0,0')

    def test_save_to_file_csv_squares(self):
        """Test saving Square instances to CSV file"""
        s1 = Square(5, 1, 3, 3)
        s2 = Square(7, 0, 0, 4)
        Square.save_to_file_csv([s1, s2])

        # Verify file exists
        self.assertTrue(os.path.exists('Square.csv'))

        # Verify file contents
        with open('Square.csv', 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 2)
            self.assertEqual(lines[0].strip(), '3,5,1,3')
            self.assertEqual(lines[1].strip(), '4,7,0,0')

    def test_load_from_file_csv_rectangles(self):
        """Test loading Rectangle instances from CSV file"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file_csv([r1, r2])

        # Load rectangles from file
        list_rectangles = Rectangle.load_from_file_csv()

        # Verify the loaded rectangles
        self.assertEqual(len(list_rectangles), 2)
        self.assertIsInstance(list_rectangles[0], Rectangle)
        self.assertIsInstance(list_rectangles[1], Rectangle)
        
        # Verify attributes of first rectangle
        self.assertEqual(list_rectangles[0].id, 1)
        self.assertEqual(list_rectangles[0].width, 10)
        self.assertEqual(list_rectangles[0].height, 7)
        self.assertEqual(list_rectangles[0].x, 2)
        self.assertEqual(list_rectangles[0].y, 8)
        
        # Verify attributes of second rectangle
        self.assertEqual(list_rectangles[1].id, 2)
        self.assertEqual(list_rectangles[1].width, 2)
        self.assertEqual(list_rectangles[1].height, 4)
        self.assertEqual(list_rectangles[1].x, 0)
        self.assertEqual(list_rectangles[1].y, 0)

    def test_load_from_file_csv_squares(self):
        """Test loading Square instances from CSV file"""
        s1 = Square(5, 1, 3, 3)
        s2 = Square(7, 0, 0, 4)
        Square.save_to_file_csv([s1, s2])

        # Load squares from file
        list_squares = Square.load_from_file_csv()

        # Verify the loaded squares
        self.assertEqual(len(list_squares), 2)
        self.assertIsInstance(list_squares[0], Square)
        self.assertIsInstance(list_squares[1], Square)
        
        # Verify attributes of first square
        self.assertEqual(list_squares[0].id, 3)
        self.assertEqual(list_squares[0].size, 5)
        self.assertEqual(list_squares[0].x, 1)
        self.assertEqual(list_squares[0].y, 3)
        
        # Verify attributes of second square
        self.assertEqual(list_squares[1].id, 4)
        self.assertEqual(list_squares[1].size, 7)
        self.assertEqual(list_squares[1].x, 0)
        self.assertEqual(list_squares[1].y, 0)

    def test_save_to_file_csv_none(self):
        """Test saving None to CSV file"""
        Rectangle.save_to_file_csv(None)
        self.assertTrue(os.path.exists('Rectangle.csv'))
        with open('Rectangle.csv', 'r') as f:
            self.assertEqual(f.read(), '')

    def test_save_to_file_csv_empty_list(self):
        """Test saving empty list to CSV file"""
        Rectangle.save_to_file_csv([])
        self.assertTrue(os.path.exists('Rectangle.csv'))
        with open('Rectangle.csv', 'r') as f:
            self.assertEqual(f.read(), '')

    def test_load_from_file_csv_no_file(self):
        """Test loading from non-existent CSV file"""
        list_rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(list_rectangles, [])

    def test_load_from_file_csv_empty_file(self):
        """Test loading from empty CSV file"""
        with open('Rectangle.csv', 'w') as f:
            f.write('')
        list_rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(list_rectangles, [])


if __name__ == '__main__':
    unittest.main()
