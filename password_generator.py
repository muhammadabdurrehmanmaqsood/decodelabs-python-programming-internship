import string
import secrets
import math
import sys

def calculate_entropy(length: int, pool_size: int) -> float:
    """
    Calculates information entropy to prove resistance to cracking techniques.
    """
    if pool_size <= 0:
        return 0.0
    return length * math.log2(pool_size)

def generate_secure_password(length: int) -> tuple[str, float]:
    """
    Generates a cryptographically secure password and calculates its entropy.
    Enforces NIST 2024 guidelines (15-64 characters).
    """
    if length < 15 or length > 64:
        raise ValueError("Length must be between 15 and 64 characters per NIST 2024 guidelines.")
        
    # Standardizing character classification for locale-independent consistency
    char_pool = string.ascii_letters + string.digits + string.punctuation
    pool_size = len(char_pool)
    
    # Utilizing secrets.choice() for hardware-level OS noise, avoiding the deterministic Mersenne Twister
    # Utilizing list comprehension and .join() to achieve O(N) time complexity and peak memory efficiency
    password_list = [secrets.choice(char_pool) for _ in range(length)]
    password = "".join(password_list)
    
    entropy = calculate_entropy(length, pool_size)
    return password, entropy
def main_cli() -> None:
    """Input-Process-Output scaffold for the terminal interface."""
    print("--- Enterprise Random Password Generator ---")
    print("NIST 2024 Standard: 15 to 64 characters.\n")
    
    while True:
        raw_input = input("Enter required password length (or 'quit' to exit): ").strip().lower()
        if raw_input == 'quit':
            print("Process terminated safely.")
            break
            
        try:
            length = int(raw_input)
            password, entropy = generate_secure_password(length)
            
            print("\n[+] SUCCESS: Secure Credential Generated")
            print(f"Password: {password}")
            print(f"Entropy:  {entropy:.2f} bits\n")
            
        except ValueError as e:
            # Catch both non-integer inputs and our custom NIST length constraints
            print(f"[-] INVALID DATA: {e}\n")

if __name__ == "__main__":
    try:
        main_cli()
    except KeyboardInterrupt:
        print("\nProcess terminated by user. Exiting safely...")
        sys.exit(0)