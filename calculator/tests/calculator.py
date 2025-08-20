import check50

@check50.check()
def exists():
    """calculator.py exists"""
    check50.exists("calculator.py")

@check50.check(exists)
def functions_defined():
    """Program defines add, subtract, multiply, and divide functions with two parameters"""
    source = open("calculator.py").read()
    for func in ["add", "subtract", "multiply", "divide"]:
        if f"def {func}(" not in source:
            raise check50.Failure(f"{func} function not found")

@check50.check(exists)
def addition():
    """Program can perform addition"""
    output = check50.run("python3 calculator.py").stdin("1\n5\n3\n5\n").stdout()
    if "8" not in output:
        raise check50.Failure("Addition result not found in output")

@check50.check(exists)
def subtraction():
    """Program can perform subtraction"""
    output = check50.run("python3 calculator.py").stdin("2\n10\n4\n5\n").stdout()
    if "6" not in output:
        raise check50.Failure("Subtraction result not found in output")

@check50.check(exists)
def multiplication():
    """Program can perform multiplication"""
    output = check50.run("python3 calculator.py").stdin("3\n4\n6\n5\n").stdout()
    if "24" not in output:
        raise check50.Failure("Multiplication result not found in output")

@check50.check(exists)
def division():
    """Program can perform division"""
    output = check50.run("python3 calculator.py").stdin("4\n20\n4\n5\n").stdout()
    if "5.0" not in output:
        raise check50.Failure("Division result not found in output")
