import check50
import check50.py

@check50.check()
def exists():
    """calculator.py exists"""
    check50.exists("calculator.py")

@check50.check(exists)
def defines_add():
    """Program defines a function called add(num1, num2)"""
    contents = open("calculator.py").read()
    if "def add(" not in contents:
        raise check50.Failure("Function add() not defined")

@check50.check(exists)
def defines_subtract():
    """Program defines a function called subtract(num1, num2)"""
    contents = open("calculator.py").read()
    if "def subtract(" not in contents:
        raise check50.Failure("Function subtract() not defined")

@check50.check(exists)
def defines_multiply():
    """Program defines a function called multiply(num1, num2)"""
    contents = open("calculator.py").read()
    if "def multiply(" not in contents:
        raise check50.Failure("Function multiply() not defined")

@check50.check(exists)
def defines_divide():
    """Program defines a function called divide(num1, num2)"""
    contents = open("calculator.py").read()
    if "def divide(" not in contents:
        raise check50.Failure("Function divide() not defined")

@check50.check(exists)
def defines_quit():
    """Program defines a function called quit_program() or similar"""
    contents = open("calculator.py").read().lower()
    if "def quit" not in contents:
        raise check50.Failure("Function to quit the program not defined")

@check50.check(exists)
def runs_operations():
    """Program can perform an addition and subtraction"""
    # We'll run the program and provide sample inputs for testing addition and subtraction
    inputs = "1\n5\n3\n5\n0\n"  # Menu choice 1=add, then 5,3; choice 2=subtract, then 5,0
    output = check50.run("python3 calculator.py").stdin(inputs).stdout(timeout=5).lower()
    if "8" not in output:
        raise check50.Failure("Addition result not displayed correctly")
    if "5" not in output:
        raise check50.Failure("Subtraction result not displayed correctly")
