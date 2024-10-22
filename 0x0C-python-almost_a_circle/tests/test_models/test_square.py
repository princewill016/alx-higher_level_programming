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

    def test_update_args(self):
        """Test update method with args"""
        s = Square(5)
        
        # Test updating id
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        
        # Test updating size
        s.update(10, 20)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 20")
        
        # Test updating x
        s.update(10, 20, 30)
        self.assertEqual(str(s), "[Square] (10) 30/0 - 20")
        
        # Test updating y
        s.update(10, 20, 30, 40)
        self.assertEqual(str(s), "[Square] (10) 30/40 - 20")

    def test_update_kwargs(self):
        """Test update method with kwargs"""
        s = Square(5)
        
        # Test updating single attribute
        s.update(size=20)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 20")
        
        # Test updating multiple attributes
        s.update(size=20, y=40, x=30, id=10)
        self.assertEqual(str(s), "[Square] (10) 30/40 - 20")
        
        # Test that args takes precedence over kwargs
        s.update(1, 2, 3, 4, size=20, y=40, x=30, id=10)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_invalid_args(self):
        """Test update method with invalid arguments"""
        s = Square(5)
        
        # Test invalid size
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(1, "invalid")
        
        # Test invalid x
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(1, 2, "invalid")
        
        # Test invalid y
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(1, 2, 3, "invalid")

    def test_update_invalid_kwargs(self):
        """Test update method with invalid kwargs"""
        s = Square(5)
        
        # Test invalid size
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")
        
        # Test invalid x
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")
        
        # Test invalid y
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")

    def test_update_with_extra_args(self):
        """Test update method with extra args"""
        s = Square(5)
        s.update(1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_with_unknown_kwargs(self):
        """Test update method with unknown kwargs"""
        s = Square(5)
        s.update(unknown=10)  # Should be ignored
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")


if __name__ == '__main__':
    unittest.main()
