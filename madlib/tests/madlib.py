import check50
import re

@check50.check()
def exists():
    """madlibs.py exists"""
    check50.exists("madlibs.py")

@check50.check(exists)
def four_inputs():
    """Program asks for at least 4 inputs"""
    source = check50.read("madlibs.py")
    input_count = len(re.findall(r"\binput\s*\(", source))
    if input_count < 4:
        raise check50.Failure(f"Found {input_count} input() calls, need at least 4")

@check50.check(exists)
def prints_story():
    """Program prints a story containing the user inputs"""
    source = check50.read("madlibs.py")
    # Check for at least one print statement
    if not re.search(r"\bprint\s*\(", source):
        raise check50.Failure("No print() statement found to display the story")
