#!/usr/bin/python3
"""
Unit tests for Rectangle class
"""
import unittest
import io
import sys
from contextlib import contextmanager
from models.rectangle import Rectangle
from models.base import Base


@contextmanager
def capture_output():
    """Capture stdout output for testing"""
    new_out = io.StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out


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

    def test_area(self):
        """Test area calculation"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    def test_display_2x2(self):
        """Test displaying a 2x2 rectangle"""
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with capture_output() as output:
            r.display()
            self.assertEqual(output.getvalue(), expected_output)

    def test_display_1x1(self):
        """Test displaying a 1x1 rectangle"""
        r = Rectangle(1, 1)
        expected_output = "#\n"
        with capture_output() as output:
            r.display()
            self.assertEqual(output.getvalue(), expected_output)

    def test_display_3x4(self):
        """Test displaying a 3x4 rectangle"""
        r = Rectangle(3, 4)
        expected_output = "###\n###\n###\n###\n"
        with capture_output() as output:
            r.display()
            self.assertEqual(output.getvalue(), expected_output)

    def test_display_4x6(self):
        """Test displaying a 4x6 rectangle"""
        r = Rectangle(4, 6)
        expected_output = "####\n####\n####\n####\n####\n####\n"
        with capture_output() as output:
            r.display()
            self.assertEqual(output.getvalue(), expected_output)

    def test_display_with_x_y(self):
        """Test that display ignores x and y values"""
        r = Rectangle(2, 3, 2, 2)
        expected_output = "##\n##\n##\n"
        with capture_output() as output:
            r.display()
            self.assertEqual(output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
