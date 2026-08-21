"""Unit tests for the expense_tracker module."""

import unittest

from expense_tracker import parse_expense


class TestExpenseTracker(unittest.TestCase):
    """Tests covering expense input parsing and validation."""

    def test_valid_integer_input(self):
        """Valid numeric strings should be converted to integers."""
        self.assertEqual(parse_expense("100"), 100)
        self.assertEqual(parse_expense("50"), 50)

    def test_invalid_string_input(self):
        """Non-numeric strings should raise ValueError."""
        with self.assertRaises(ValueError):
            parse_expense("ten")

    def test_empty_input(self):
        """Empty strings should raise ValueError."""
        with self.assertRaises(ValueError):
            parse_expense("")


if __name__ == "__main__":
    unittest.main()
