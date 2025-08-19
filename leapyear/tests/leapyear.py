import check50

@check50.check()
def exists():
    """leap.py exists"""
    check50.exists("leap.py")

@check50.check(exists)
def defines_function():
    """is_leap_year function is defined"""
    check50.run("python3 -c 'import leap; leap.is_leap_year'")

@check50.check(defines_function)
def test_2024():
    """is_leap_year(2024) returns True"""
    check50.run("python3 -c 'import leap; print(leap.is_leap_year(2024))'").stdout("True\n")

@check50.check(defines_function)
def test_1900():
    """is_leap_year(1900) returns False"""
    check50.run("python3 -c 'import leap; print(leap.is_leap_year(1900))'").stdout("False\n")

@check50.check(defines_function)
def test_1600():
    """is_leap_year(1600) returns True"""
    check50.run("python3 -c 'import leap; print(leap.is_leap_year(1600))'").stdout("True\n")

@check50.check(defines_function)
def test_2001():
    """is_leap_year(2001) returns False"""
    check50.run("python3 -c 'import leap; print(leap.is_leap_year(2001))'").stdout("False\n")
