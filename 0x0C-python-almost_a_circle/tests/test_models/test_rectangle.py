#!/usr/bin/python3
"""
Unit tests for Rectangle class
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def setUp(self):
        """Reset __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_basic_initialization(self):
        """Test basic initialization with width and height"""
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_full_initialization(self):
        """Test initialization with all attributes"""
        r = Rectangle(10, 20, 1, 2, 100)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 100)

    def test_width_validation_on_init(self):
        """Test width validation during initialization"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 20)

    def test_height_validation_on_init(self):
        """Test height validation during initialization"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "20")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -20)

    def test_x_validation_on_init(self):
        """Test x validation during initialization"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, "1")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 20, -1)

    def test_y_validation_on_init(self):
        """Test y validation during initialization"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 1, "2")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 20, 1, -2)

    def test_area(self):
        """Test area calculation"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)
        
        r3 = Rectangle(2, 10)
        self.assertEqual(r3.area(), 20)
        
        # Test with larger numbers
        r4 = Rectangle(999, 999)
        self.assertEqual(r4.area(), 998001)

    def test_area_after_attribute_change(self):
        """Test area calculation after changing attributes"""
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)
        
        r.width = 5
        self.assertEqual(r.area(), 15)
        
        r.height = 7
        self.assertEqual(r.area(), 35)


if __name__ == '__main__':
    unittest.main()
