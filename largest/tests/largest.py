import check50
import sys

@check50.check()
def exists():
    """largest.py exists"""
    check50.exists("largest.py")

@check50.check(exists)
def test_first_largest():
    """largest(10, 5, 3) returns 10"""
    sys.path.insert(0, '.')
    import largest
    
    result = largest.largest(10, 5, 3)
    
    if result != 10:
        raise check50.Failure(f"Expected 10, got {result}")

@check50.check(exists)
def test_second_largest():
    """largest(5, 20, 8) returns 20"""
    sys.path.insert(0, '.')
    import largest
    
    result = largest.largest(5, 20, 8)
    
    if result != 20:
        raise check50.Failure(f"Expected 20, got {result}")

@check50.check(exists)
def test_third_largest():
    """largest(3, 7, 15) returns 15"""
    sys.path.insert(0, '.')
    import largest
    
    result = largest.largest(3, 7, 15)
    
    if result != 15:
        raise check50.Failure(f"Expected 15, got {result}")

@check50.check(exists)
def test_all_equal():
    """largest(5, 5, 5) returns 5"""
    sys.path.insert(0, '.')
    import largest
    
    result = largest.largest(5, 5, 5)
    
    if result != 5:
        raise check50.Failure(f"Expected 5, got {result}")

@check50.check(exists)
def test_two_equal_largest():
    """largest(10, 10, 3) returns 10"""
    sys.path.insert(0, '.')
    import largest
    
    result = largest.largest(10, 10, 3)
    
    if result != 10:
        raise check50.Failure(f"Expected 10, got {result}")

@check50.check(exists)
def test_negative_numbers():
    """largest(-5, -2, -10) returns -2"""
    sys.path.insert(0, '.')
    import largest
    
    result = largest.largest(-5, -2, -10)
    
    if result != -2:
        raise check50.Failure(f"Expected -2, got {result}")

@check50.check(exists)
def test_mixed_positive_negative():
    """largest(-10, 0, 5) returns 5"""
    sys.path.insert(0, '.')
    import largest
    
    result = largest.largest(-10, 0, 5)
    
    if result != 5:
        raise check50.Failure(f"Expected 5, got {result}")

@check50.check(exists)
def test_zero_included():
    """largest(0, 0, 0) returns 0"""
    sys.path.insert(0, '.')
    import largest
    
    result = largest.largest(0, 0, 0)
    
    if result != 0:
        raise check50.Failure(f"Expected 0, got {result}")
