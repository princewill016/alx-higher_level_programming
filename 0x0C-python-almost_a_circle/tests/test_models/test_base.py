#!/usr/bin/python3
"""
Unit tests for Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def setUp(self):
        """Set up test method"""
        self.r1 = Rectangle(10, 10)

    def test_update_no_args(self):
        """Test update method with no arguments"""
        r = Rectangle(10, 10, 10, 10, 10)
        initial_dict = r.__dict__.copy()
        r.update()
        self.assertEqual(r.__dict__, initial_dict)

    def test_update_one_arg(self):
        """Test update method with one argument (id)"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)
        # Check other attributes remain unchanged
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_update_two_args(self):
        """Test update method with two arguments (id, width)"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        # Check other attributes remain unchanged
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_update_three_args(self):
        """Test update method with three arguments (id, width, height)"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        # Check other attributes remain unchanged
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_update_four_args(self):
        """Test update method with four arguments (id, width, height, x)"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        # Check other attribute remains unchanged
        self.assertEqual(r.y, 10)

    def test_update_five_args(self):
        """Test update method with five arguments (id, width, height, x, y)"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_more_than_five_args(self):
        """Test update method with more than five arguments"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6, 7, 8)
        # Only first five should be used
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_invalid_width_type(self):
        """Test update method with invalid width type"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_invalid_height_type(self):
        """Test update method with invalid height type"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_invalid_x_type(self):
        """Test update method with invalid x type"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")

    def test_update_invalid_y_type(self):
        """Test update method with invalid y type"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")


if __name__ == '__main__':
    unittest.main()
