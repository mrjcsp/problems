import check50
import sys

@check50.check()
def exists():
    """grade.py exists"""
    check50.exists("grade.py")

@check50.check(exists)
def test_a_grade_90():
    """grade(90) returns A"""
    sys.path.insert(0, '.')
    import grade
    
    result = grade.grade(90)
    
    if result != "A":
        raise check50.Failure(f"Expected 'A', got '{result}'")

@check50.check(exists)
def test_a_grade_95():
    """grade(95) returns A"""
    sys.path.insert(0, '.')
    import grade
    
    result = grade.grade(95)
    
    if result != "A":
        raise check50.Failure(f"Expected 'A', got '{result}'")

@check50.check(exists)
def test_a_grade_100():
    """grade(100) returns A"""
    sys.path.insert(0, '.')
    import grade
    
    result = grade.grade(100)
    
    if result != "A":
        raise check50.Failure(f"Expected 'A', got '{result}'")

@check50.check(exists)
def test_b_grade_80():
    """grade(80) returns B"""
    sys.path.insert(0, '.')
    import grade
    
    result = grade.grade(80)
    
    if result != "B":
        raise check50.Failure(f"Expected 'B', got '{result}'")

@check50.check(exists)
def test_b_grade_85():
    """grade(85) returns B"""
    sys.path.insert(0, '.')
    import grade
    
    result = grade.grade(85)
    
    if result != "B":
        raise check50.Failure(f"Expected 'B', got '{result}'")

@check50.check(exists)
def test_b_grade_89():
    """grade(89) returns B"""
    sys.path.insert(0, '.')
    import grade
    
    result = grade.grade(89)
    
    if result != "B":
        raise check50.Failure(f"Expected 'B', got '{result}'")

@check50.check(exists)
def test_c_grade_70():
    """grade(70) returns C"""
    sys.path.insert(0, '.')
    import grade
    
    result = grade.grade(70)
    
    if result != "C":
        raise check50.Failure(f"Expected 'C', got '{result}'")

@check50.check(exists)
def test_c_grade_75():
    """grade(75) returns C"""
    sys.path.insert(0, '.')
    import grade
    
    result = grade.grade(75)
    
    if result != "C":
        raise check50.Failure(f"Expected 'C', got '{result}'")

@check50.check(exists)
def test_c_grade_79():
    """grade(79) returns C"""
    sys.path.insert(0, '.')
    import grade
    
    result = grade.grade(79)
    
    if result != "C":
        raise check50.Failure(f"Expected 'C', got '{result}'")

@check50.check(exists)
def test_d_grade_60():
    """grade(60) returns D"""
    sys.path.insert(0, '.')
    import grade
    
    result = grade.grade(60)
    
    if result != "D":
        raise check50.Failure(f"Expected 'D', got '{result}'")

@check50.check(exists)
def test_d_grade_65():
    """grade(65) returns D"""
    sys.path.insert(0, '.')
    import grade
    
    result = grade.grade(65)
    
    if result != "D":
        raise check50.Failure(f"Expected 'D', got '{result}'")

@check50.check(exists)
def test_d_grade_69():
    """grade(69) returns D"""
    sys.path.insert(0, '.')
    import grade
    
    result = grade.grade(69)
    
    if result != "D":
        raise check50.Failure(f"Expected 'D', got '{result}'")

@check50.check(exists)
def test_f_grade_59():
    """grade(59) returns F"""
    sys.path.insert(0, '.')
    import grade
    
    result = grade.grade(59)
    
    if result != "F":
        raise check50.Failure(f"Expected 'F', got '{result}'")

@check50.check(exists)
def test_f_grade_50():
    """grade(50) returns F"""
    sys.path.insert(0, '.')
    import grade
    
    result = grade.grade(50)
    
    if result != "F":
        raise check50.Failure(f"Expected 'F', got '{result}'")

@check50.check(exists)
def test_f_grade_0():
    """grade(0) returns F"""
    sys.path.insert(0, '.')
    import grade
    
    result = grade.grade(0)
    
    if result != "F":
        raise check50.Failure(f"Expected 'F', got '{result}'")
