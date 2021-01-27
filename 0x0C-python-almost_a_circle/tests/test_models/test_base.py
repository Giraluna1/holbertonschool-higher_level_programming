#!/usr/bin/python3
""" Module Unittest for base"""

import unittest
import pep8
import inspect


from models.base import Base


class TestBase(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
