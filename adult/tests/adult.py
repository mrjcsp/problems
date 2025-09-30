import check50
import check50.py

@check50.check()
def exists():
    """adult.py exists"""
    check50.exists("adult.py")

@check50.check(exists)
def function_defined():
    """Program defines a function is_adult(age)"""
    student = check50.py.import_("adult")
    if not hasattr(student, "is_adult"):
        raise check50.Failure("Function is_adult not defined")

@check50.check(function_defined)
def under_18_returns_false():
    """is_adult(17) returns False"""
    student = check50.py.import_("adult")
    if student.is_adult(17) != False:
        raise check50.Failure("is_adult(17) should return False")

@check50.check(function_defined)
def over_18_returns_true():
    """is_adult(18) returns True"""
    student = check50.py.import_("adult")
    if student.is_adult(18) != True:
        raise check50.Failure("is_adult(18) should return True")

@check50.check(function_defined)
def older_returns_true():
    """is_adult(30) returns True"""
    student = check50.py.import_("adult")
    if student.is_adult(30) != True:
        raise check50.Failure("is_adult(30) should return True")
