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

    def test_update_args(self):
        """Test update method with no-keyword arguments"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args_kwargs(self):
        """Test update with both args and kwargs (args should take precedence)"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_kwargs(self):
        """Test update method with keyword arguments"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=1, width=2, y=3, x=4, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 4/3 - 2/1")

    def test_update_kwargs_partial(self):
        """Test update with some keyword arguments"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=1, width=2)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.id, 10)

    def test_update_kwargs_invalid_attr(self):
        """Test update with invalid attribute name"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(invalid_attr=1)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_kwargs_invalid_value_type(self):
        """Test update with invalid value type"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.update(width="invalid")

    def test_update_empty_args_kwargs(self):
        """Test update with empty args and kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_args_with_none(self):
        """Test update with None as argument"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        self.assertIsNone(r.id)

    def test_update_kwargs_with_none(self):
        """Test update with None as keyword argument"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        self.assertIsNone(r.id)


if __name__ == '__main__':
    unittest.main()
