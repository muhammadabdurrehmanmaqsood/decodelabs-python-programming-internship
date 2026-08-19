import unittest
from expense_tracker import parse_expense

class TestExpenseTracker(unittest.TestCase):
    
    def test_valid_integer_input(self):
        """Test that valid string integers are transformed correctly."""
        self.assertEqual(parse_expense("100"), 100)
        self.assertEqual(parse_expense("50"), 50)
        
    def test_invalid_string_input(self):
        """Test that the Poka-Yoke mechanism triggers a ValueError on bad data."""
        with self.assertRaises(ValueError):
            parse_expense("ten")
            
    def test_empty_input(self):
        """Test that empty strings are caught by the error handler."""
        with self.assertRaises(ValueError):
            parse_expense("")

if __name__ == '__main__':
    unittest.main()