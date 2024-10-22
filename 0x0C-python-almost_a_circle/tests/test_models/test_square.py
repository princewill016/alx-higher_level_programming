#!/usr/bin/python3
"""
Unit test module for the Square class.
This module contains comprehensive test cases for all Square class functionality.
"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    Tests instantiation, attributes, methods, and inheritance behavior.
    """

    def setUp(self):
        """Reset Base._nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_square_inheritance(self):
        """Test that Square inherits from Rectangle"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_square_instantiation(self):
        """Test Square instantiation with various parameters"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

        s2 = Square(10, 2)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.id, 2)

        s3 = Square(3, 1, 3)
        self.assertEqual(s3.size, 3)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.id, 3)

        s4 = Square(2, 1, 2, 12)
        self.assertEqual(s4.size, 2)
        self.assertEqual(s4.x, 1)
        self.assertEqual(s4.y, 2)
        self.assertEqual(s4.id, 12)

    def test_invalid_attributes(self):
        """Test validation of attributes"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "2")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 2, "3")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 2, -3)

    def test_area(self):
        """Test area calculation"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s2 = Square(10)
        self.assertEqual(s2.area(), 100)

    def test_str_representation(self):
        """Test string representation"""
        s1 = Square(5, 1, 2, 10)
        self.assertEqual(str(s1), "[Square] (10) 1/2 - 5")

    def test_size_property(self):
        """Test size getter and setter"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = "10"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.size = 0

    def test_update_args(self):
        """Test update method with *args"""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(10, 2)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 2")
        s1.update(10, 2, 3)
        self.assertEqual(str(s1), "[Square] (10) 3/0 - 2")
        s1.update(10, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (10) 3/4 - 2")

    def test_update_kwargs(self):
        """Test update method with **kwargs"""
        s1 = Square(5)
        s1.update(size=10)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        s1.update(size=11, x=2)
        self.assertEqual(str(s1), "[Square] (1) 2/0 - 11")
        s1.update(y=3, size=12, x=1)
        self.assertEqual(str(s1), "[Square] (1) 1/3 - 12")

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        s1 = Square(5, 2, 3, 10)
        s1_dict = s1.to_dictionary()
        expected_dict = {'id': 10, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s1_dict, expected_dict)
        
        # Test that changing the dictionary doesn't affect the Square
        s1_dict['size'] = 20
        self.assertEqual(s1.size, 5)
        
        # Test creating a new Square with the dictionary
        s2 = Square(1)
        s2.update(**s1_dict)
        self.assertEqual(str(s2), "[Square] (10) 2/3 - 20")

    def test_empty_creation(self):
        """Test creation of Square with no arguments"""
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_arguments(self):
        """Test creation of Square with too many arguments"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)


if __name__ == '__main__':
    unittest.main()
