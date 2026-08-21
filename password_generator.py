"""Cryptographically secure password generator.

Generates passwords using the `secrets` module (suitable for
security-sensitive contexts, unlike the `random` module) and reports
the resulting Shannon entropy so users can judge password strength.
"""

import math
import secrets
import string
import sys
from typing import Tuple

MIN_LENGTH = 15
MAX_LENGTH = 64


def calculate_entropy(length: int, pool_size: int) -> float:
    """Calculate the Shannon entropy of a randomly generated string.

    Args:
        length: Number of characters in the generated string.
        pool_size: Number of distinct characters available per position.

    Returns:
        Entropy in bits. Returns 0.0 if the pool size is non-positive.
    """
    if pool_size <= 0:
        return 0.0
    return length * math.log2(pool_size)


def generate_secure_password(length: int) -> Tuple[str, float]:
    """Generate a cryptographically secure password and its entropy.

    Enforces NIST 2024 guidance of 15-64 characters per password.

    Args:
        length: Desired password length.

    Returns:
        A tuple of (password, entropy_in_bits).

    Raises:
        ValueError: If length is outside the 15-64 character range.
    """
    if length < MIN_LENGTH or length > MAX_LENGTH:
        raise ValueError(
            f"Length must be between {MIN_LENGTH} and {MAX_LENGTH} "
            "characters per NIST 2024 guidelines."
        )

    # secrets.choice() draws from the OS's cryptographically secure
    # random source, unlike the deterministic `random` module.
    char_pool = string.ascii_letters + string.digits + string.punctuation
    pool_size = len(char_pool)
    password = "".join(secrets.choice(char_pool) for _ in range(length))

    entropy = calculate_entropy(length, pool_size)
    return password, entropy


def main_cli() -> None:
    """Run the interactive password generator command-line interface."""
    print("--- Secure Password Generator ---")
    print(f"NIST 2024 Standard: {MIN_LENGTH} to {MAX_LENGTH} characters.\n")

    while True:
        raw_input = input("Enter required password length (or 'quit' to exit): ").strip().lower()
        if raw_input == "quit":
            print("Process terminated safely.")
            break

        try:
            length = int(raw_input)
            password, entropy = generate_secure_password(length)

            print("\n[+] SUCCESS: Secure Credential Generated")
            print(f"Password: {password}")
            print(f"Entropy:  {entropy:.2f} bits\n")

        except ValueError as error:
            # Catches both non-integer input and NIST length violations.
            print(f"[-] INVALID DATA: {error}\n")


if __name__ == "__main__":
    try:
        main_cli()
    except KeyboardInterrupt:
        print("\nProcess terminated by user. Exiting safely...")
        sys.exit(0)
