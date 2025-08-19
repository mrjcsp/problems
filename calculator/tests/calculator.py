import check50
import re

@check50.check()
def exists():
    """calculator.py exists"""
    check50.exists("calculator.py")

@check50.check(exists)
def functions_defined():
    """Program defines add, subtract, multiply, and divide functions with two parameters"""
    source = check50.read("calculator.py")
    for func in ["add", "subtract", "multiply", "divide"]:
        # Use regex to check function signature with exactly two parameters
        pattern = rf"def {func}\(\s*\w+\s*,\s*\w+\s*\)"
        if not re.search(pattern, source):
            raise check50.Failure(f"{func}() not defined with two parameters")

@check50.check(exists)
def addition():
    """Program can perform addition correctly"""
    out = check50.run("python3 calculator.py").stdin("1\n3\n7\n\n5\n").stdout()
    if "Result: 10" not in out and "Result: 10.0" not in out:
        raise check50.Failure("Addition result not correct")

@check50.check(exists)
def subtraction():
    """Program can perform subtraction correctly"""
    out = check50.run("python3 calculator.py").stdin("2\n10\n4\n\n5\n").stdout()
    if "Result: 6" not in out and "Result: 6.0" not in out:
        raise check50.Failure("Subtraction result not correct")

@check50.check(exists)
def multiplication():
    """Program can perform multiplication correctly"""
    out = check50.run("python3 calculator.py").stdin("3\n5\n2\n\n5\n").stdout()
    if "Result: 10" not in out and "Result: 10.0" not in out:
        raise check50.Failure("Multiplication result not correct")

@check50.check(exists)
def division():
    """Program can perform division correctly"""
    out = check50.run("python3 calculator.py").stdin("4\n8\n2\n\n5\n").stdout()
    if "Result: 4" not in out and "Result: 4.0" not in out:
        raise check50.Failure("Division result not correct")
