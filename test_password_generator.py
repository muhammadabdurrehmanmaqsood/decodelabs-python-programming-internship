import unittest
from password_generator import generate_secure_password, calculate_entropy

class TestPasswordGenerator(unittest.TestCase):
    
    def test_valid_generation_and_entropy(self):
        """Test that valid lengths produce correct output strings and safe entropy."""
        password, entropy = generate_secure_password(16)
        self.assertEqual(len(password), 16)
        self.assertGreater(entropy, 100.0) 
        
    def test_nist_minimum_length_rejection(self):
        """Test that lengths under 15 characters are blocked per NIST guidelines."""
        with self.assertRaises(ValueError):
            generate_secure_password(14)
            
    def test_nist_maximum_length_rejection(self):
        """Test that lengths over 64 characters are blocked to prevent buffer strain."""
        with self.assertRaises(ValueError):
            generate_secure_password(65)
            
    def test_entropy_math(self):
        """Verify the E = L * log2(R) mathematical formula."""
        # A length of 10 with a pool of 4 should yield exactly 20.0 bits of entropy
        self.assertEqual(calculate_entropy(10, 4), 20.0)

if __name__ == '__main__':
    unittest.main()