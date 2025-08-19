import check50
import re

@check50.check()
def exists():
    """guess.py exists"""
    check50.exists("guess.py")

# --- REQUIRED FUNCTIONALITY ---

@check50.check(exists)
def correct_guess():
    """Program congratulates the user for a correct guess"""
    output = check50.run("python3 -c 'import random; random.randint=lambda a,b: 7; import guess'").stdin("7\n").stdout()
    if not re.search(r"congrat", output, re.IGNORECASE):
        raise check50.Failure("Expected congratulatory message when guess is correct")

@check50.check(exists)
def incorrect_guess():
    """Program reveals the number when the guess is wrong"""
    output = check50.run("python3 -c 'import random; random.randint=lambda a,b: 7; import guess'").stdin("3\n").stdout()
    if "7" not in output:
        raise check50.Failure("Expected program to reveal the correct number after wrong guess")
    if not re.search(r"wrong|lose|incorrect", output, re.IGNORECASE):
        raise check50.Failure("Expected message indicating the guess was wrong")

# --- EXTRA CHALLENGE: KEEP GUESSING UNTIL CORRECT ---

@check50.check(exists)
def too_high_too_low():
    """Program gives 'too high' or 'too low' feedback when incorrect"""
    run = check50.run("python3 -c 'import random; random.randint=lambda a,b: 7; import guess'")
    output = run.stdin("3\n").stdout(timeout=2)  # too low
    output += run.stdin("9\n").stdout(timeout=2)  # too high
    if not re.search(r"low", output, re.IGNORECASE):
        raise check50.Failure("Expected feedback 'too low' for a guess below the secret number")
    if not re.search(r"high", output, re.IGNORECASE):
        raise check50.Failure("Expected feedback 'too high' for a guess above the secret number")

@check50.check(exists)
def loop_until_correct():
    """Program allows multiple guesses until correct"""
    run = check50.run("python3 -c 'import random; random.randint=lambda a,b: 7; import guess'")
    run.stdin("3\n")  # wrong
    run.stdin("5\n")  # wrong
    output = run.stdin("7\n").stdout(timeout=2)  # correct
    if not re.search(r"congrat", output, re.IGNORECASE):
        raise check50.Failure("Expected congratulatory message after eventually guessing correctly")

# --- EXTRA EXTRA CHALLENGE: DIFFICULTY + GUESS LIMIT ---

@check50.check(exists)
def difficulty_setting():
    """Program supports difficulty levels (Easy/Medium/Hard)"""
    run = check50.run("python3 -c 'import random; random.randint=lambda a,b: 7; import guess'")
    output = run.stdin("Easy\n7\n").stdout(timeout=2)
    if not re.search(r"congrat", output, re.IGNORECASE):
        raise check50.Failure("Expected to win on Easy difficulty with correct guess")

@check50.check(exists)
def guess_limit():
    """Program enforces a guess limit (e.g., 3 tries)"""
    run = check50.run("python3 -c 'import random; random.randint=lambda a,b: 7; import guess'")
    run.stdin("1\n")  # wrong
    run.stdin("2\n")  # wrong
    output = run.stdin("3\n").stdout(timeout=2)  # wrong again (3rd)
    if not re.search(r"lose|out of guesses|game over", output, re.IGNORECASE):
        raise check50.Failure("Expected message about losing after using all allowed guesses")
