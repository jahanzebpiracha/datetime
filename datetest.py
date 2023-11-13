import unittest
from harnesspythontest import get_current_year, is_leap_year

class Testharnesspythontest(unittest.TestCase):

    def test_get_current_year(self):
        current_year = get_current_year()
        self.assertIsInstance(current_year, int)
        self.assertGreaterEqual(current_year, 2000)  # Adjust the starting year as needed

    def test_is_leap_year(self):
        # Test with known leap years
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2020))
        self.assertTrue(is_leap_year(2400))

        # Test with known non-leap years
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2100))
        self.assertFalse(is_leap_year(2200))

if __name__ == '__main__':
    unittest.main()
