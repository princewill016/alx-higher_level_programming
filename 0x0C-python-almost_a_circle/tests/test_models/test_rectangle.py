#!/usr/bin/python3
"""
Unit tests for Rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_str(self):
        """Test __str__ method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1, 0, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

        r3 = Rectangle(1, 1, 0, 0, 99)
        self.assertEqual(str(r3), "[Rectangle] (99) 0/0 - 1/1")


if __name__ == '__main__':
    unittest.main()
