"""Command-line expense tracker.

Reads a running list of expense amounts from the user, validates
each entry, and reports a running and final total.
"""

import sys


def parse_expense(user_input: str) -> int:
    """Validate and convert raw user input into an integer amount.

    Args:
        user_input: The raw string entered by the user.

    Returns:
        The parsed integer expense amount.

    Raises:
        ValueError: If the input cannot be converted to an integer.
    """
    return int(user_input)


def run_tracker() -> None:
    """Run the interactive expense-tracking loop until the user quits.

    Continuously prompts for expense amounts, accumulating a running
    total, until the user enters 'quit'. Invalid entries are rejected
    with a message and do not affect the total.
    """
    total = 0

    print("--- DecodeLabs Expense Tracker ---")
    print("Enter an expense amount to add to the total.")
    print("Type 'quit' to stop and view the final total.\n")

    while True:
        raw_input = input("Enter expense: ").strip().lower()

        if raw_input == "quit":
            break

        try:
            new_expense = parse_expense(raw_input)
            total += new_expense
            print(f"Accepted. Current Total: ${total}")
        except ValueError:
            print("Invalid input: please enter a valid whole number.")

    print(f"\nFINAL TOTAL: ${total}")


if __name__ == "__main__":
    try:
        run_tracker()
    except KeyboardInterrupt:
        print("\nProcess terminated by user. Exiting safely...")
        sys.exit(0)
