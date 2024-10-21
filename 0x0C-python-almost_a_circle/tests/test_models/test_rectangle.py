#!/usr/bin/python3
"""
Unit tests for Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_str_method_width_height(self):
        """Test __str__ method with width and height"""
        r = Rectangle(1, 2)
        self.assertEqual(str(r), "[Rectangle] ({}) 0/0 - 1/2".format(r.id))

    def test_str_method_width_height_x(self):
        """Test __str__ method with width, height, x"""
        r = Rectangle(1, 2, 3)
        self.assertEqual(str(r), "[Rectangle] ({}) 3/0 - 1/2".format(r.id))

    def test_str_method_width_height_x_y(self):
        """Test __str__ method with width, height, x, y"""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] ({}) 3/4 - 1/2".format(r.id))

    def test_str_method_width_height_x_y_id(self):
        """Test __str__ method with all attributes"""
        r = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(str(r), "[Rectangle] (50) 30/40 - 10/20")

    def test_str_method_changed_attributes(self):
        """Test __str__ method with changed attributes"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.width = 2
        r.height = 3
        r.x = 4
        r.y = 5
        self.assertEqual(str(r), "[Rectangle] (1) 4/5 - 2/3")

    def test_str_method_one_arg(self):
        """Test __str__ method with one argument"""
        with self.assertRaises(TypeError):
            Rectangle(1)


if __name__ == '__main__':
    unittest.main()
