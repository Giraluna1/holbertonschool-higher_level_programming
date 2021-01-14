#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_interger(self):
        """Test output of max_interger()
        """
        self.assertAlmostEqual(max_integer([1, 2, 5, 4, 7]), 7)
        self.assertAlmostEqual(max_integer([-7, 2, -1, 3, 5]), 5)
        self.assertAlmostEqual(max_integer([0]), 0)
        self.assertAlmostEqual(max_integer([2, 2, 2]), 2)
        self.assertAlmostEqual(max_integer([-1, 0, 1]), 1)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer([1, 2, 6, 4, 5]), 6)
        self.assertAlmostEqual(max_integer([6, 2, 4, 4, 5]), 6)
