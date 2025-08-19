import check50
import re

@check50.check()
def exists():
    """guess.py exists"""
    check50.exists("guess.py")

@check50.check(exists)
def has_function():
    """guess.py defines a function called guessing_game"""
    import guess
    if not hasattr(guess, "guessing_game"):
        raise check50.Failure("No function called guessing_game() found")

@check50.check(has_function)
def output_message():
    """Program outputs either a win or loss message with a number"""
    import guess
    import io
    import sys

    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        guess.guessing_game()
        output = sys.stdout.getvalue().lower()
    finally:
        sys.stdout = old_stdout

    # Check for win or loss
    if not ("congrat" in output or "sorry" in output or "lose" in output):
        raise check50.Failure("Output should contain a congratulations or loss message")

    # Check for a number 1-10
    numbers = re.findall(r"\b([1-9]|10)\b", output)
    if not numbers:
        raise check50.Failure("Output should include a number between 1 and 10 (the secret number)")
