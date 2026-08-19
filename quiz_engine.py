import sys

def evaluate_question(prompt: str, expected_answer: str) -> int:
    """
    Executes the Question Block Micro-Architecture:
    Ask/Capture -> Sanitize -> Evaluate -> Execute.
    Returns 1 for a correct answer, 0 for incorrect.
    """
    # Step 1: Ask & Capture (Input Gateway)
    raw_input = input(f"{prompt}\n> ")

    # Step 2: Sanitize (Whitespace Audit & Data Normalization)
    # .strip() removes accidental keystrokes/tabs; .casefold() ensures robust caseless matching
    sanitized_input = raw_input.strip().casefold()

    # Step 3 & 4: Evaluate & Execute (Logic Gate)
    if sanitized_input == expected_answer.casefold():
        print("[+] Correct!\n")
        return 1
    else:
        print(f"[-] Incorrect. The correct answer is '{expected_answer}'.\n")
        return 0

def run_quiz() -> None:
    """Main IPOS execution loop."""
    print("=" * 50)
    print(" ENTERPRISE DECISION ENGINE: KNOWLEDGE QUIZ")
    print("=" * 50 + "\n")

    # Storage: State Initialization (Type Integrity)
    score = 0 

    # Process: Sequential Control Flow via Rule Engines
    score += evaluate_question(
        prompt="Q1: What is the capital of France?",
        expected_answer="paris"
    )
    
    score += evaluate_question(
        prompt="Q2: Which planet in our solar system is known as the Red Planet?",
        expected_answer="mars"
    )
    
    score += evaluate_question(
        prompt="Q3: What is the chemical symbol for water?",
        expected_answer="h2o"
    )

    # Output: Feedback & Output Clarity (F-String Injector)
    print("=" * 50)
    print(" ASSESSMENT COMPLETE")
    print("-" * 50)
    # Demonstrating dynamic f-string alignment per architectural standards
    print(f" FINAL SCORE:{score:>20} / 3")
    print("=" * 50)

if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        # Graceful shutdown handler
        print("\n\n[!] Process interrupted by user. Shutting down safely.")
        sys.exit(0)