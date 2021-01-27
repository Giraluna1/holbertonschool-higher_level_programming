#!/usr/bin/python3
""" Module Unittest for Square"""

import unittest
import pep8


from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test the class Square """
    def test_pep8_conformance_square(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
