import check50
import check50.py

@check50.check()
def exists():
    """madlibs.py exists"""
    check50.exists("madlibs.py")

@check50.check(exists)
def asks_for_inputs():
    """Program asks for at least 4 inputs"""
    code = open("madlibs.py").read()
    num_inputs = code.count("input(")
    if num_inputs < 4:
        raise check50.Failure("Program should call input() at least 4 times")

@check50.check(exists)
def prints_story():
    """Program prints a story containing the user inputs"""
    code = open("madlibs.py").read()
    if "print(" not in code:
        raise check50.Failure("Program should print the final story")
