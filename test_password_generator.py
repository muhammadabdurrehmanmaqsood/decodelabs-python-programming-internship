"""Unit tests for the password_generator module."""

import unittest

from password_generator import calculate_entropy, generate_secure_password


class TestPasswordGenerator(unittest.TestCase):
    """Tests covering password generation and entropy calculation."""

    def test_valid_generation_and_entropy(self):
        """Valid lengths should produce correctly sized, high-entropy passwords."""
        password, entropy = generate_secure_password(16)
        self.assertEqual(len(password), 16)
        self.assertGreater(entropy, 100.0)

    def test_nist_minimum_length_rejection(self):
        """Lengths under 15 characters should be rejected per NIST guidelines."""
        with self.assertRaises(ValueError):
            generate_secure_password(14)

    def test_nist_maximum_length_rejection(self):
        """Lengths over 64 characters should be rejected per NIST guidelines."""
        with self.assertRaises(ValueError):
            generate_secure_password(65)

    def test_entropy_math(self):
        """Entropy should follow E = L * log2(R)."""
        # A length of 10 with a pool of 4 yields exactly 20.0 bits of entropy.
        self.assertEqual(calculate_entropy(10, 4), 20.0)


if __name__ == "__main__":
    unittest.main()
