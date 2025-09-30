import check50
import sys
import io
from unittest.mock import patch
from contextlib import redirect_stdout

@check50.check()
def exists():
    """login.py exists"""
    check50.exists("login.py")

@check50.check(exists)
def test_correct_credentials():
    """login() with correct username and password prints success message"""
    sys.path.insert(0, '.')
    
    # Mock input to provide correct credentials BEFORE importing
    with patch('builtins.input', side_effect=['YourUsername', 'YourPassword']):
        f = io.StringIO()
        with redirect_stdout(f):
            # Import inside the mock context
            if 'login' in sys.modules:
                del sys.modules['login']
            import login
        output = f.getvalue().lower()
        
        # Check if output contains success indicators
        if not any(word in output for word in ['success', 'welcome', 'correct', 'logged in', 'login successful']):
            raise check50.Failure(f"Expected success message, got '{f.getvalue().strip()}'")

@check50.check(exists)
def test_correct_credentials_lowercase():
    """login() with lowercase username 'yourusername' prints success message"""
    sys.path.insert(0, '.')
    
    # Mock input with lowercase username
    with patch('builtins.input', side_effect=['yourusername', 'YourPassword']):
        f = io.StringIO()
        with redirect_stdout(f):
            if 'login' in sys.modules:
                del sys.modules['login']
            import login
        output = f.getvalue().lower()
        
        # Check if output contains success indicators
        if not any(word in output for word in ['success', 'welcome', 'correct', 'logged in', 'login successful']):
            raise check50.Failure(f"Expected success message (case-insensitive username), got '{f.getvalue().strip()}'")

@check50.check(exists)
def test_correct_credentials_uppercase():
    """login() with uppercase username 'YOURUSERNAME' prints success message"""
    sys.path.insert(0, '.')
    
    # Mock input with uppercase username
    with patch('builtins.input', side_effect=['YOURUSERNAME', 'YourPassword']):
        f = io.StringIO()
        with redirect_stdout(f):
            if 'login' in sys.modules:
                del sys.modules['login']
            import login
        output = f.getvalue().lower()
        
        # Check if output contains success indicators
        if not any(word in output for word in ['success', 'welcome', 'correct', 'logged in', 'login successful']):
            raise check50.Failure(f"Expected success message (case-insensitive username), got '{f.getvalue().strip()}'")

@check50.check(exists)
def test_wrong_username():
    """login() with wrong username prints failure message"""
    sys.path.insert(0, '.')
    
    # Mock input with wrong username
    with patch('builtins.input', side_effect=['WrongUser', 'YourPassword']):
        f = io.StringIO()
        with redirect_stdout(f):
            if 'login' in sys.modules:
                del sys.modules['login']
            import login
        output = f.getvalue().lower()
        
        # Check if output contains failure indicators
        if not any(word in output for word in ['invalid', 'incorrect', 'wrong', 'failed', 'error', 'denied']):
            raise check50.Failure(f"Expected failure message, got '{f.getvalue().strip()}'")

@check50.check(exists)
def test_wrong_password():
    """login() with wrong password prints failure message"""
    sys.path.insert(0, '.')
    
    # Mock input with wrong password
    with patch('builtins.input', side_effect=['YourUsername', 'WrongPassword']):
        f = io.StringIO()
        with redirect_stdout(f):
            if 'login' in sys.modules:
                del sys.modules['login']
            import login
        output = f.getvalue().lower()
        
        # Check if output contains failure indicators
        if not any(word in output for word in ['invalid', 'incorrect', 'wrong', 'failed', 'error', 'denied']):
            raise check50.Failure(f"Expected failure message, got '{f.getvalue().strip()}'")

@check50.check(exists)
def test_both_wrong():
    """login() with wrong username and password prints failure message"""
    sys.path.insert(0, '.')
    
    # Mock input with both wrong
    with patch('builtins.input', side_effect=['WrongUser', 'WrongPassword']):
        f = io.StringIO()
        with redirect_stdout(f):
            if 'login' in sys.modules:
                del sys.modules['login']
            import login
        output = f.getvalue().lower()
        
        # Check if output contains failure indicators
        if not any(word in output for word in ['invalid', 'incorrect', 'wrong', 'failed', 'error', 'denied']):
            raise check50.Failure(f"Expected failure message, got '{f.getvalue().strip()}'")

@check50.check(exists)
def test_password_case_sensitive():
    """login() with correct username but wrong password case prints failure message"""
    sys.path.insert(0, '.')
    
    # Mock input with wrong password case
    with patch('builtins.input', side_effect=['YourUsername', 'yourpassword']):
        f = io.StringIO()
        with redirect_stdout(f):
            if 'login' in sys.modules:
                del sys.modules['login']
            import login
        output = f.getvalue().lower()
        
        # Check if output contains failure indicators (password should be case-sensitive)
        if not any(word in output for word in ['invalid', 'incorrect', 'wrong', 'failed', 'error', 'denied']):
            raise check50.Failure(f"Expected failure message (password is case-sensitive), got '{f.getvalue().strip()}'")
