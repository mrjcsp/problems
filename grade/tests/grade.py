import check50
import sys
import io
from contextlib import redirect_stdout

@check50.check()
def exists():
    """grade.py exists"""
    check50.exists("grade.py")

@check50.check(exists)
def test_a_grade_90():
    """grade(90) prints A"""
    sys.path.insert(0, '.')
    import grade
    
    f = io.StringIO()
    with redirect_stdout(f):
        grade.grade(90)
    output = f.getvalue().strip()
    
    if output != "A":
        raise check50.Failure(f"Expected 'A', got '{output}'")

@check50.check(exists)
def test_a_grade_95():
    """grade(95) prints A"""
    sys.path.insert(0, '.')
    import grade
    
    f = io.StringIO()
    with redirect_stdout(f):
        grade.grade(95)
    output = f.getvalue().strip()
    
    if output != "A":
        raise check50.Failure(f"Expected 'A', got '{output}'")

@check50.check(exists)
def test_a_grade_100():
    """grade(100) prints A"""
    sys.path.insert(0, '.')
    import grade
    
    f = io.StringIO()
    with redirect_stdout(f):
        grade.grade(100)
    output = f.getvalue().strip()
    
    if output != "A":
        raise check50.Failure(f"Expected 'A', got '{output}'")

@check50.check(exists)
def test_b_grade_80():
    """grade(80) prints B"""
    sys.path.insert(0, '.')
    import grade
    
    f = io.StringIO()
    with redirect_stdout(f):
        grade.grade(80)
    output = f.getvalue().strip()
    
    if output != "B":
        raise check50.Failure(f"Expected 'B', got '{output}'")

@check50.check(exists)
def test_b_grade_85():
    """grade(85) prints B"""
    sys.path.insert(0, '.')
    import grade
    
    f = io.StringIO()
    with redirect_stdout(f):
        grade.grade(85)
    output = f.getvalue().strip()
    
    if output != "B":
        raise check50.Failure(f"Expected 'B', got '{output}'")

@check50.check(exists)
def test_b_grade_89():
    """grade(89) prints B"""
    sys.path.insert(0, '.')
    import grade
    
    f = io.StringIO()
    with redirect_stdout(f):
        grade.grade(89)
    output = f.getvalue().strip()
    
    if output != "B":
        raise check50.Failure(f"Expected 'B', got '{output}'")

@check50.check(exists)
def test_c_grade_70():
    """grade(70) prints C"""
    sys.path.insert(0, '.')
    import grade
    
    f = io.StringIO()
    with redirect_stdout(f):
        grade.grade(70)
    output = f.getvalue().strip()
    
    if output != "C":
        raise check50.Failure(f"Expected 'C', got '{output}'")

@check50.check(exists)
def test_c_grade_75():
    """grade(75) prints C"""
    sys.path.insert(0, '.')
    import grade
    
    f = io.StringIO()
    with redirect_stdout(f):
        grade.grade(75)
    output = f.getvalue().strip()
    
    if output != "C":
        raise check50.Failure(f"Expected 'C', got '{output}'")

@check50.check(exists)
def test_c_grade_79():
    """grade(79) prints C"""
    sys.path.insert(0, '.')
    import grade
    
    f = io.StringIO()
    with redirect_stdout(f):
        grade.grade(79)
    output = f.getvalue().strip()
    
    if output != "C":
        raise check50.Failure(f"Expected 'C', got '{output}'")

@check50.check(exists)
def test_d_grade_60():
    """grade(60) prints D"""
    sys.path.insert(0, '.')
    import grade
    
    f = io.StringIO()
    with redirect_stdout(f):
        grade.grade(60)
    output = f.getvalue().strip()
    
    if output != "D":
        raise check50.Failure(f"Expected 'D', got '{output}'")

@check50.check(exists)
def test_d_grade_65():
    """grade(65) prints D"""
    sys.path.insert(0, '.')
    import grade
    
    f = io.StringIO()
    with redirect_stdout(f):
        grade.grade(65)
    output = f.getvalue().strip()
    
    if output != "D":
        raise check50.Failure(f"Expected 'D', got '{output}'")

@check50.check(exists)
def test_d_grade_69():
    """grade(69) prints D"""
    sys.path.insert(0, '.')
    import grade
    
    f = io.StringIO()
    with redirect_stdout(f):
        grade.grade(69)
    output = f.getvalue().strip()
    
    if output != "D":
        raise check50.Failure(f"Expected 'D', got '{output}'")

@check50.check(exists)
def test_f_grade_59():
    """grade(59) prints F"""
    sys.path.insert(0, '.')
    import grade
    
    f = io.StringIO()
    with redirect_stdout(f):
        grade.grade(59)
    output = f.getvalue().strip()
    
    if output != "F":
        raise check50.Failure(f"Expected 'F', got '{output}'")

@check50.check(exists)
def test_f_grade_50():
    """grade(50) prints F"""
    sys.path.insert(0, '.')
    import grade
    
    f = io.StringIO()
    with redirect_stdout(f):
        grade.grade(50)
    output = f.getvalue().strip()
    
    if output != "F":
        raise check50.Failure(f"Expected 'F', got '{output}'")

@check50.check(exists)
def test_f_grade_0():
    """grade(0) prints F"""
    sys.path.insert(0, '.')
    import grade
    
    f = io.StringIO()
    with redirect_stdout(f):
        grade.grade(0)
    output = f.getvalue().strip()
    
    if output != "F":
        raise check50.Failure(f"Expected 'F', got '{output}'")
