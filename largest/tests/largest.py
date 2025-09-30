import check50
import sys
import io
from contextlib import redirect_stdout

@check50.check()
def exists():
    """largest.py exists"""
    check50.exists("largest.py")

@check50.check(exists)
def test_first_largest():
    """print_largest(10, 5, 3) prints 10"""
    sys.path.insert(0, '.')
    import largest
    
    f = io.StringIO()
    with redirect_stdout(f):
        largest.print_largest(10, 5, 3)
    output = f.getvalue().strip()
    
    if output != "10":
        raise check50.Failure(f"Expected '10', got '{output}'")

@check50.check(exists)
def test_second_largest():
    """print_largest(5, 20, 8) prints 20"""
    sys.path.insert(0, '.')
    import largest
    
    f = io.StringIO()
    with redirect_stdout(f):
        largest.print_largest(5, 20, 8)
    output = f.getvalue().strip()
    
    if output != "20":
        raise check50.Failure(f"Expected '20', got '{output}'")

@check50.check(exists)
def test_third_largest():
    """print_largest(3, 7, 15) prints 15"""
    sys.path.insert(0, '.')
    import largest
    
    f = io.StringIO()
    with redirect_stdout(f):
        largest.print_largest(3, 7, 15)
    output = f.getvalue().strip()
    
    if output != "15":
        raise check50.Failure(f"Expected '15', got '{output}'")

@check50.check(exists)
def test_all_equal():
    """print_largest(5, 5, 5) prints 5"""
    sys.path.insert(0, '.')
    import largest
    
    f = io.StringIO()
    with redirect_stdout(f):
        largest.print_largest(5, 5, 5)
    output = f.getvalue().strip()
    
    if output != "5":
        raise check50.Failure(f"Expected '5', got '{output}'")

@check50.check(exists)
def test_two_equal_largest():
    """print_largest(10, 10, 3) prints 10"""
    sys.path.insert(0, '.')
    import largest
    
    f = io.StringIO()
    with redirect_stdout(f):
        largest.print_largest(10, 10, 3)
    output = f.getvalue().strip()
    
    if output != "10":
        raise check50.Failure(f"Expected '10', got '{output}'")

@check50.check(exists)
def test_negative_numbers():
    """print_largest(-5, -2, -10) prints -2"""
    sys.path.insert(0, '.')
    import largest
    
    f = io.StringIO()
    with redirect_stdout(f):
        largest.print_largest(-5, -2, -10)
    output = f.getvalue().strip()
    
    if output != "-2":
        raise check50.Failure(f"Expected '-2', got '{output}'")

@check50.check(exists)
def test_mixed_positive_negative():
    """print_largest(-10, 0, 5) prints 5"""
    sys.path.insert(0, '.')
    import largest
    
    f = io.StringIO()
    with redirect_stdout(f):
        largest.print_largest(-10, 0, 5)
    output = f.getvalue().strip()
    
    if output != "5":
        raise check50.Failure(f"Expected '5', got '{output}'")

@check50.check(exists)
def test_zero_included():
    """print_largest(0, 0, 0) prints 0"""
    sys.path.insert(0, '.')
    import largest
    
    f = io.StringIO()
    with redirect_stdout(f):
        largest.print_largest(0, 0, 0)
    output = f.getvalue().strip()
    
    if output != "0":
        raise check50.Failure(f"Expected '0', got '{output}'")
