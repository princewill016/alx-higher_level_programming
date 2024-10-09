#!/usr/bin/python3
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the max_integer function.
    """

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_duplicate_elements(self):
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4])

if __name__ == "__main__":
    unittest.main()
