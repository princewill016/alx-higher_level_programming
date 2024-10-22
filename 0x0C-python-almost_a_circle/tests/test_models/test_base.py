#!/usr/bin/python3
"""Unit tests for Base class draw method"""
import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseDraw(unittest.TestCase):
    """Test cases for Base class draw method"""

    @classmethod
    def setUpClass(cls):
        """Set up test class"""
        Base._Base__nb_objects = 0

    def setUp(self):
        """Set up test method"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    @patch('turtle.Screen')
    @patch('turtle.Turtle')
    def test_draw_empty_lists(self, mock_turtle, mock_screen):
        """Test draw method with empty lists"""
        Base.draw([], [])
        mock_turtle.assert_called_once()
        mock_screen.assert_called_once()

    @patch('turtle.Screen')
    @patch('turtle.Turtle')
    def test_draw_rectangles(self, mock_turtle, mock_screen):
        """Test draw method with rectangles"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Base.draw([r1, r2], [])
        mock_turtle.assert_called_once()
        mock_screen.assert_called_once()

    @patch('turtle.Screen')
    @patch('turtle.Turtle')
    def test_draw_squares(self, mock_turtle, mock_screen):
        """Test draw method with squares"""
        s1 = Square(10, 7, 2)
        s2 = Square(8)
        Base.draw([], [s1, s2])
        mock_turtle.assert_called_once()
        mock_screen.assert_called_once()

    @patch('turtle.Screen')
    @patch('turtle.Turtle')
    def test_draw_both(self, mock_turtle, mock_screen):
        """Test draw method with both rectangles and squares"""
        r1 = Rectangle(10, 7, 2, 8)
        s1 = Square(10, 7, 2)
        Base.draw([r1], [s1])
        mock_turtle.assert_called_once()
        mock_screen.assert_called_once()

if __name__ == '__main__':
    unittest.main()
