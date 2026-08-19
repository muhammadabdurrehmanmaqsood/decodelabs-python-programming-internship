import sys

def parse_expense(user_input: str) -> int:
    """
    Validates and transforms raw input into an integer.
    Raises ValueError if the input is not a valid integer.
    """
    # The int() transformation mechanism enforces type-safety
    return int(user_input)

def run_tracker() -> None:
    """
    Executes the continuous audit loop, accumulates expenses,
    and handles the graceful shutdown via sentinel value.
    """
    total = 0  # State initialized outside the loop
    
    print("--- DecodeLabs Expense Tracker ---")
    print("Enter an expense amount to add to the total.")
    print("Type 'quit' to halt execution and view the final total.\n")
    
    while True:
        raw_input = input("Enter expense: ").strip().lower()
        
        # Kill switch / Sentinel path
        if raw_input == 'quit':
            break
            
        # Poka-Yoke mechanism (Error-proofing)
        try:
            new_expense = parse_expense(raw_input)
            total += new_expense  # Accumulator pattern: State(new) = State(old) + Input
            print(f"Accepted. Current Total: ${total}")
        except ValueError:
            print("Invalid Data: Please enter a valid numerical integer.")
            
    # Output Stream
    print(f"\nFINAL TOTAL: ${total}")

if __name__ == "__main__":
    try:
        run_tracker()
    except KeyboardInterrupt:
        print("\nProcess terminated by user. Exiting safely...")
        sys.exit(0)