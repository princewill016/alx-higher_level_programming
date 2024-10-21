#!/usr/bin/python3
"""
Unit tests for Base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def setUp(self):
        """Reset __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_id_given(self):
        """Test initialization with given id"""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none(self):
        """Test initialization with id=None"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_multiple_instances(self):
        """Test creation of multiple instances"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_mixed_ids(self):
        """Test mixed automatic and manual id assignment"""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_id_string(self):
        """Test initialization with string id"""
        b = Base("hello")
        self.assertEqual(b.id, "hello")


if __name__ == '__main__':
    unittest.main()
