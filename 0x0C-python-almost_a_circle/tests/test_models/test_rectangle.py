#!/usr/bin/python3
""" Module Unittest for Rectangle"""

import unittest
import pep8


from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test the class Rectangle """
    def test_pep8_conformance_rectangle(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
