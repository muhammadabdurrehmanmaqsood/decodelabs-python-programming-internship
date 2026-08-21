"""Command-line knowledge quiz engine.

Asks the user a fixed set of general-knowledge questions, checks
answers case-insensitively, and reports a final score.
"""

import sys
from typing import List, Tuple

QUESTIONS: List[Tuple[str, str]] = [
    ("Q1: What is the capital of France?", "paris"),
    ("Q2: Which planet in our solar system is known as the Red Planet?", "mars"),
    ("Q3: What is the chemical symbol for water?", "h2o"),
]


def evaluate_question(prompt: str, expected_answer: str) -> int:
    """Ask a single question and check the user's answer.

    Args:
        prompt: The question text to display.
        expected_answer: The correct answer, compared case-insensitively.

    Returns:
        1 if the answer is correct, 0 otherwise.
    """
    raw_input = input(f"{prompt}\n> ")
    sanitized_input = raw_input.strip().casefold()

    if sanitized_input == expected_answer.casefold():
        print("[+] Correct!\n")
        return 1

    print(f"[-] Incorrect. The correct answer is '{expected_answer}'.\n")
    return 0


def run_quiz() -> None:
    """Run the full quiz and print the final score."""
    print("=" * 50)
    print(" KNOWLEDGE QUIZ")
    print("=" * 50 + "\n")

    score = sum(
        evaluate_question(prompt, answer) for prompt, answer in QUESTIONS
    )

    print("=" * 50)
    print(" ASSESSMENT COMPLETE")
    print("-" * 50)
    print(f" FINAL SCORE:{score:>20} / {len(QUESTIONS)}")
    print("=" * 50)


if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\n\n[!] Process interrupted by user. Shutting down safely.")
        sys.exit(0)
