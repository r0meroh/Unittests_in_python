import unittest
from format_a_name import format_name

"""
This file tests both objects with the assertEqual tests to compare
input values with the expected values that the program should return.
"""


class NamesTestCase(unittest.TestCase):
    """test for the format name function"""

    def test_first(self):
        """test names with middle names"""
        test_name = format_name('John', '', 'Doe')
        self.assertEqual(test_name, 'John  Doe')

    def test_with_middle(self):
        """test names with middle names"""
        test_name = format_name('Jane', 'Nancy', 'Doe')
        self.assertEqual(test_name, 'Jane Nancy Doe')


if __name__ == '__main__':
    unittest.main()
