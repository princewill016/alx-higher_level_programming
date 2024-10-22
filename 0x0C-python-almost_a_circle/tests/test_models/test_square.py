#!/usr/bin/python3
"""
Unit tests for Square class
"""
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class
    """

    def setUp(self):
        """Set up test cases"""
        Square._Base__nb_objects = 0

    def test_inheritance(self):
        """Test if Square inherits from Rectangle"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_initialization(self):
        """Test initialization of Square instance"""
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

        s2 = Square(2, 3, 4, 5)
        self.assertEqual(s2.width, 2)
        self.assertEqual(s2.height, 2)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 4)
        self.assertEqual(s2.id, 5)

    def test_size_property(self):
        """Test size getter and setter"""
        s = Square(5)
        self.assertEqual(s.size, 5)
        
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.size, 10)

    def test_str_method(self):
        """Test __str__ method"""
        s = Square(4, 2, 1, 12)
        expected = "[Square] (12) 2/1 - 4"
        self.assertEqual(str(s), expected)

    def test_invalid_size_type(self):
        """Test size validation for type"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_invalid_size_value(self):
        """Test size validation for value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

    def test_invalid_x(self):
        """Test x validation"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "2")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -2)

    def test_invalid_y(self):
        """Test y validation"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 2, "3")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 2, -3)

    def test_area(self):
        """Test area calculation"""
        s = Square(5)
        self.assertEqual(s.area(), 25)
        
        s.size = 10
        self.assertEqual(s.area(), 100)

    def test_display(self):
        """Test that display method exists"""
        s = Square(2)
        self.assertTrue(hasattr(s, 'display'))

    def test_update_args(self):
        """Test update method with *args"""
        s = Square(5)
        s.update(10, 20, 30, 40)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 30)
        self.assertEqual(s.y, 40)

    def test_update_kwargs(self):
        """Test update method with **kwargs"""
        s = Square(5)
        s.update(size=20, y=40, x=30, id=10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 30)
        self.assertEqual(s.y, 40)


if __name__ == '__main__':
    unittest.main()
