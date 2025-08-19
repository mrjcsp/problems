import check50
import check50.py

@check50.check()
def exists():
    """guess.py exists"""
    check50.exists("guess.py")

@check50.check(exists)
def imports_random():
    """Program imports the random module"""
    contents = open("guess.py").read()
    if "import random" not in contents:
        raise check50.Failure("random module not imported")

@check50.check(exists)
def defines_function():
    """Program defines a function called guessing_game()"""
    contents = open("guess.py").read()
    if "def guessing_game" not in contents:
        raise check50.Failure("Function guessing_game() not defined")

@check50.check(exists)
def prints_result():
    """Program outputs either a congrats message or a loss message"""
    # Provide a sample guess input
    result = check50.run("python3 guess.py").stdin("5\n").stdout(timeout=5)
    success_msgs = ["congratulations", "correct number"]
    failure_msgs = ["sorry", "better luck"]
    output = result.lower()
    if not any(msg in output for msg in success_msgs + failure_msgs):
        raise check50.Failure("No congratulatory or loss message detected")
