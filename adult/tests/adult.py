import check50

@check50.check()
def exists():
    """adult.py exists"""
    check50.exists("adult.py")

@check50.check(exists)
def function_defined():
    """Program defines a function is_adult(age)"""
    namespace = {}
    exec(open("adult.py").read(), namespace)
    if "is_adult" not in namespace:
        raise check50.Failure("Function is_adult not defined")

@check50.check(function_defined)
def test_under_18():
    """is_adult(17) returns False"""
    namespace = {}
    exec(open("adult.py").read(), namespace)
    result = namespace 
    if not isinstance(result, bool):
        raise check50.Failure("Function should return a boolean (True/False), not " + str(type(result)))
    if result != False:
        raise check50.Failure("is_adult(17) should return False")

@check50.check(function_defined)
def test_equal_18():
    """is_adult(18) returns True"""
    namespace = {}
    exec(open("adult.py").read(), namespace)
    result = namespace 
    if not isinstance(result, bool):
        raise check50.Failure("Function should return a boolean (True/False), not " + str(type(result)))
    if result != True:
        raise check50.Failure("is_adult(18) should return True")

@check50.check(function_defined)
def test_above_18():
    """is_adult(30) returns True"""
    namespace = {}
    exec(open("adult.py").read(), namespace)
    r
