import check50
import sys
import io
from unittest.mock import patch
from contextlib import redirect_stdout

@check50.check()
def exists():
    """ticket.py exists"""
    check50.exists("ticket.py")

@check50.check(exists)
def test_adult_weekday():
    """Adult on weekday pays $100"""
    sys.path.insert(0, '.')
    if 'ticket' in sys.modules:
        del sys.modules['ticket']
    
    import ticket
    
    with patch('builtins.input', side_effect=['John Doe', '25', 'Monday', '']):
        f = io.StringIO()
        with redirect_stdout(f):
            ticket.ticket()
        output = f.getvalue()
        
        if '100' not in output:
            raise check50.Failure(f"Expected price $100 for adult on weekday, output:\n{output}")

@check50.check(exists)
def test_adult_weekend():
    """Adult on weekend pays $100"""
    sys.path.insert(0, '.')
    if 'ticket' in sys.modules:
        del sys.modules['ticket']
    
    import ticket
    
    with patch('builtins.input', side_effect=['Jane Smith', '30', 'Saturday', '']):
        f = io.StringIO()
        with redirect_stdout(f):
            ticket.ticket()
        output = f.getvalue()
        
        if '100' not in output:
            raise check50.Failure(f"Expected price $100 for adult on weekend, output:\n{output}")

@check50.check(exists)
def test_toddler_free():
    """Child age 3 or under is free"""
    sys.path.insert(0, '.')
    if 'ticket' in sys.modules:
        del sys.modules['ticket']
    
    import ticket
    
    with patch('builtins.input', side_effect=['Baby Smith', '2', 'Wednesday', '']):
        f = io.StringIO()
        with redirect_stdout(f):
            ticket.ticket()
        output = f.getvalue().lower()
        
        if not ('0' in output or 'free' in output):
            raise check50.Failure(f"Expected price $0 or 'free' for toddler, output:\n{output}")

@check50.check(exists)
def test_child_weekday():
    """Child (age 4-17) on weekday pays $50"""
    sys.path.insert(0, '.')
    if 'ticket' in sys.modules:
        del sys.modules['ticket']
    
    import ticket
    
    with patch('builtins.input', side_effect=['Tommy Lee', '10', 'Tuesday', '']):
        f = io.StringIO()
        with redirect_stdout(f):
            ticket.ticket()
        output = f.getvalue()
        
        if '50' not in output:
            raise check50.Failure(f"Expected price $50 for child on weekday, output:\n{output}")

@check50.check(exists)
def test_child_weekend():
    """Child (age 4-17) on weekend pays $100"""
    sys.path.insert(0, '.')
    if 'ticket' in sys.modules:
        del sys.modules['ticket']
    
    import ticket
    
    with patch('builtins.input', side_effect=['Sarah Johnson', '12', 'Sunday', '']):
        f = io.StringIO()
        with redirect_stdout(f):
            ticket.ticket()
        output = f.getvalue()
        
        if '100' not in output:
            raise check50.Failure(f"Expected price $100 for child on weekend, output:\n{output}")

@check50.check(exists)
def test_student_weekday():
    """Student (age 17) on weekday pays $50"""
    sys.path.insert(0, '.')
    if 'ticket' in sys.modules:
        del sys.modules['ticket']
    
    import ticket
    
    with patch('builtins.input', side_effect=['Alex Brown', '17', 'Thursday', '']):
        f = io.StringIO()
        with redirect_stdout(f):
            ticket.ticket()
        output = f.getvalue()
        
        if '50' not in output:
            raise check50.Failure(f"Expected price $50 for student on weekday, output:\n{output}")

@check50.check(exists)
def test_freefriday_coupon():
    """Child with FREEFRIDAY coupon on Friday is free"""
    sys.path.insert(0, '.')
    if 'ticket' in sys.modules:
        del sys.modules['ticket']
    
    import ticket
    
    with patch('builtins.input', side_effect=['Emma Davis', '8', 'Friday', 'FREEFRIDAY']):
        f = io.StringIO()
        with redirect_stdout(f):
            ticket.ticket()
        output = f.getvalue().lower()
        
        if not ('0' in output or 'free' in output):
            raise check50.Failure(f"Expected price $0 or 'free' for child with FREEFRIDAY on Friday, output:\n{output}")

@check50.check(exists)
def test_freefriday_wrong_day():
    """Child with FREEFRIDAY coupon on non-Friday still pays regular price"""
    sys.path.insert(0, '.')
    if 'ticket' in sys.modules:
        del sys.modules['ticket']
    
    import ticket
    
    with patch('builtins.input', side_effect=['Mike Wilson', '9', 'Monday', 'FREEFRIDAY']):
        f = io.StringIO()
        with redirect_stdout(f):
            ticket.ticket()
        output = f.getvalue()
        
        if '50' not in output:
            raise check50.Failure(f"Expected price $50 for child with FREEFRIDAY on Monday (weekday), output:\n{output}")

@check50.check(exists)
def test_sunday10_coupon():
    """Child with SUNDAY10 coupon on Sunday pays $90"""
    sys.path.insert(0, '.')
    if 'ticket' in sys.modules:
        del sys.modules['ticket']
    
    import ticket
    
    with patch('builtins.input', side_effect=['Lisa Garcia', '15', 'Sunday', 'SUNDAY10']):
        f = io.StringIO()
        with redirect_stdout(f):
            ticket.ticket()
        output = f.getvalue()
        
        if '90' not in output:
            raise check50.Failure(f"Expected price $90 for child with SUNDAY10 on Sunday (100-10), output:\n{output}")

@check50.check(exists)
def test_sunday10_wrong_day():
    """Child with SUNDAY10 coupon on non-Sunday pays regular price"""
    sys.path.insert(0, '.')
    if 'ticket' in sys.modules:
        del sys.modules['ticket']
    
    import ticket
    
    with patch('builtins.input', side_effect=['Chris Martinez', '14', 'Wednesday', 'SUNDAY10']):
        f = io.StringIO()
        with redirect_stdout(f):
            ticket.ticket()
        output = f.getvalue()
        
        if '50' not in output:
            raise check50.Failure(f"Expected price $50 for child with SUNDAY10 on Wednesday (weekday), output:\n{output}")

@check50.check(exists)
def test_displays_name():
    """Ticket displays customer name"""
    sys.path.insert(0, '.')
    if 'ticket' in sys.modules:
        del sys.modules['ticket']
    
    import ticket
    
    with patch('builtins.input', side_effect=['TestName123', '25', 'Monday', '']):
        f = io.StringIO()
        with redirect_stdout(f):
            ticket.ticket()
        output = f.getvalue()
        
        if 'TestName123' not in output:
            raise check50.Failure(f"Expected name 'TestName123' to be displayed in ticket, output:\n{output}")

@check50.check(exists)
def test_displays_day():
    """Ticket displays day of the week"""
    sys.path.insert(0, '.')
    if 'ticket' in sys.modules:
        del sys.modules['ticket']
    
    import ticket
    
    with patch('builtins.input', side_effect=['John Doe', '25', 'Wednesday', '']):
        f = io.StringIO()
        with redirect_stdout(f):
            ticket.ticket()
        output = f.getvalue()
        
        if 'Wednesday' not in output and 'wednesday' not in output.lower():
            raise check50.Failure(f"Expected day 'Wednesday' to be displayed in ticket, output:\n{output}")

@check50.check(exists)
def test_case_insensitive_coupon():
    """Coupon codes work case-insensitively (freefriday)"""
    sys.path.insert(0, '.')
    if 'ticket' in sys.modules:
        del sys.modules['ticket']
    
    import ticket
    
    with patch('builtins.input', side_effect=['Test User', '10', 'Friday', 'freefriday']):
        f = io.StringIO()
        with redirect_stdout(f):
            ticket.ticket()
        output = f.getvalue().lower()
        
        if not ('0' in output or 'free' in output):
            raise check50.Failure(f"Expected coupon code to work case-insensitively, output:\n{output}")

@check50.check(exists)
def test_adult_not_affected_by_coupon():
    """Adults are not affected by children's coupon codes"""
    sys.path.insert(0, '.')
    if 'ticket' in sys.modules:
        del sys.modules['ticket']
    
    import ticket
    
    with patch('builtins.input', side_effect=['Adult Test', '30', 'Friday', 'FREEFRIDAY']):
        f = io.StringIO()
        with redirect_stdout(f):
            ticket.ticket()
        output = f.getvalue()
        
        if '100' not in output:
            raise check50.Failure(f"Expected adult to still pay $100 even with FREEFRIDAY code, output:\n{output}")
