import check50
import sys
import io
from unittest.mock import patch
from contextlib import redirect_stdout
import re

@check50.check()
def exists():
    """rps.py exists"""
    check50.exists("rps.py")

@check50.check(exists)
def test_player_wins_rock_scissors():
    """Player wins with rock vs scissors"""
    sys.path.insert(0, '.')
    if 'rps' in sys.modules:
        del sys.modules['rps']
    
    # Mock: player chooses rock, computer chooses scissors (via random), then quit
    with patch('builtins.input', side_effect=['rock', 'quit']):
        with patch('random.choice', return_value='scissors'):
            f = io.StringIO()
            with redirect_stdout(f):
                try:
                    import rps
                except (SystemExit, KeyboardInterrupt):
                    pass
            output = f.getvalue().lower()
            
            # Check that player won
            if not any(word in output for word in ['you win', 'player win', 'you won', 'player won']):
                raise check50.Failure(f"Expected player to win (rock beats scissors), output:\n{f.getvalue()}")

@check50.check(exists)
def test_player_wins_scissors_paper():
    """Player wins with scissors vs paper"""
    sys.path.insert(0, '.')
    if 'rps' in sys.modules:
        del sys.modules['rps']
    
    with patch('builtins.input', side_effect=['scissors', 'quit']):
        with patch('random.choice', return_value='paper'):
            f = io.StringIO()
            with redirect_stdout(f):
                try:
                    import rps
                except (SystemExit, KeyboardInterrupt):
                    pass
            output = f.getvalue().lower()
            
            if not any(word in output for word in ['you win', 'player win', 'you won', 'player won']):
                raise check50.Failure(f"Expected player to win (scissors beats paper), output:\n{f.getvalue()}")

@check50.check(exists)
def test_player_wins_paper_rock():
    """Player wins with paper vs rock"""
    sys.path.insert(0, '.')
    if 'rps' in sys.modules:
        del sys.modules['rps']
    
    with patch('builtins.input', side_effect=['paper', 'quit']):
        with patch('random.choice', return_value='rock'):
            f = io.StringIO()
            with redirect_stdout(f):
                try:
                    import rps
                except (SystemExit, KeyboardInterrupt):
                    pass
            output = f.getvalue().lower()
            
            if not any(word in output for word in ['you win', 'player win', 'you won', 'player won']):
                raise check50.Failure(f"Expected player to win (paper beats rock), output:\n{f.getvalue()}")

@check50.check(exists)
def test_computer_wins_rock_paper():
    """Computer wins with paper vs player's rock"""
    sys.path.insert(0, '.')
    if 'rps' in sys.modules:
        del sys.modules['rps']
    
    with patch('builtins.input', side_effect=['rock', 'quit']):
        with patch('random.choice', return_value='paper'):
            f = io.StringIO()
            with redirect_stdout(f):
                try:
                    import rps
                except (SystemExit, KeyboardInterrupt):
                    pass
            output = f.getvalue().lower()
            
            if not any(word in output for word in ['computer win', 'you lose', 'player lose', 'computer won', 'you lost']):
                raise check50.Failure(f"Expected computer to win (paper beats rock), output:\n{f.getvalue()}")

@check50.check(exists)
def test_computer_wins_scissors_rock():
    """Computer wins with rock vs player's scissors"""
    sys.path.insert(0, '.')
    if 'rps' in sys.modules:
        del sys.modules['rps']
    
    with patch('builtins.input', side_effect=['scissors', 'quit']):
        with patch('random.choice', return_value='rock'):
            f = io.StringIO()
            with redirect_stdout(f):
                try:
                    import rps
                except (SystemExit, KeyboardInterrupt):
                    pass
            output = f.getvalue().lower()
            
            if not any(word in output for word in ['computer win', 'you lose', 'player lose', 'computer won', 'you lost']):
                raise check50.Failure(f"Expected computer to win (rock beats scissors), output:\n{f.getvalue()}")

@check50.check(exists)
def test_computer_wins_paper_scissors():
    """Computer wins with scissors vs player's paper"""
    sys.path.insert(0, '.')
    if 'rps' in sys.modules:
        del sys.modules['rps']
    
    with patch('builtins.input', side_effect=['paper', 'quit']):
        with patch('random.choice', return_value='scissors'):
            f = io.StringIO()
            with redirect_stdout(f):
                try:
                    import rps
                except (SystemExit, KeyboardInterrupt):
                    pass
            output = f.getvalue().lower()
            
            if not any(word in output for word in ['computer win', 'you lose', 'player lose', 'computer won', 'you lost']):
                raise check50.Failure(f"Expected computer to win (scissors beats paper), output:\n{f.getvalue()}")

@check50.check(exists)
def test_tie_rock():
    """Tie when both choose rock"""
    sys.path.insert(0, '.')
    if 'rps' in sys.modules:
        del sys.modules['rps']
    
    with patch('builtins.input', side_effect=['rock', 'quit']):
        with patch('random.choice', return_value='rock'):
            f = io.StringIO()
            with redirect_stdout(f):
                try:
                    import rps
                except (SystemExit, KeyboardInterrupt):
                    pass
            output = f.getvalue().lower()
            
            if 'tie' not in output and 'draw' not in output:
                raise check50.Failure(f"Expected tie when both choose rock, output:\n{f.getvalue()}")

@check50.check(exists)
def test_tie_paper():
    """Tie when both choose paper"""
    sys.path.insert(0, '.')
    if 'rps' in sys.modules:
        del sys.modules['rps']
    
    with patch('builtins.input', side_effect=['paper', 'quit']):
        with patch('random.choice', return_value='paper'):
            f = io.StringIO()
            with redirect_stdout(f):
                try:
                    import rps
                except (SystemExit, KeyboardInterrupt):
                    pass
            output = f.getvalue().lower()
            
            if 'tie' not in output and 'draw' not in output:
                raise check50.Failure(f"Expected tie when both choose paper, output:\n{f.getvalue()}")

@check50.check(exists)
def test_tie_scissors():
    """Tie when both choose scissors"""
    sys.path.insert(0, '.')
    if 'rps' in sys.modules:
        del sys.modules['rps']
    
    with patch('builtins.input', side_effect=['scissors', 'quit']):
        with patch('random.choice', return_value='scissors'):
            f = io.StringIO()
            with redirect_stdout(f):
                try:
                    import rps
                except (SystemExit, KeyboardInterrupt):
                    pass
            output = f.getvalue().lower()
            
            if 'tie' not in output and 'draw' not in output:
                raise check50.Failure(f"Expected tie when both choose scissors, output:\n{f.getvalue()}")

@check50.check(exists)
def test_score_tracking():
    """Score is tracked and displayed after each round"""
    sys.path.insert(0, '.')
    if 'rps' in sys.modules:
        del sys.modules['rps']
    
    # Player wins twice, computer wins once
    computer_choices = ['scissors', 'paper', 'scissors']
    with patch('builtins.input', side_effect=['rock', 'scissors', 'rock', 'quit']):
        with patch('random.choice', side_effect=computer_choices):
            f = io.StringIO()
            with redirect_stdout(f):
                try:
                    import rps
                except (SystemExit, KeyboardInterrupt):
                    pass
            output = f.getvalue().lower()
            
            # Look for score display patterns
            if not any(pattern in output for pattern in ['player', 'score', 'win']):
                raise check50.Failure(f"Expected score to be displayed, output:\n{f.getvalue()}")
            
            # Check for numbers indicating scores
            if not re.search(r'\d', output):
                raise check50.Failure(f"Expected numeric scores to be displayed, output:\n{f.getvalue()}")

@check50.check(exists)
def test_invalid_input_handling():
    """Invalid input is handled gracefully"""
    sys.path.insert(0, '.')
    if 'rps' in sys.modules:
        del sys.modules['rps']
    
    with patch('builtins.input', side_effect=['invalid', 'rock', 'quit']):
        with patch('random.choice', return_value='scissors'):
            f = io.StringIO()
            with redirect_stdout(f):
                try:
                    import rps
                except (SystemExit, KeyboardInterrupt):
                    pass
            output = f.getvalue().lower()
            
            # Should either ask again or show error message
            if 'invalid' not in output and 'error' not in output and 'try again' not in output:
                # Alternative: just continues without crashing
                if 'you win' not in output and 'player win' not in output:
                    raise check50.Failure(f"Expected invalid input handling, output:\n{f.getvalue()}")

@check50.check(exists)
def test_case_insensitive():
    """Accepts uppercase/mixed case input (ROCK, Rock, etc.)"""
    sys.path.insert(0, '.')
    if 'rps' in sys.modules:
        del sys.modules['rps']
    
    with patch('builtins.input', side_effect=['ROCK', 'quit']):
        with patch('random.choice', return_value='scissors'):
            f = io.StringIO()
            with redirect_stdout(f):
                try:
                    import rps
                except (SystemExit, KeyboardInterrupt):
                    pass
            output = f.getvalue().lower()
            
            if not any(word in output for word in ['you win', 'player win', 'you won', 'player won']):
                raise check50.Failure(f"Expected case-insensitive input (ROCK should work), output:\n{f.getvalue()}")

@check50.check(exists)
def test_multiple_rounds():
    """Program allows multiple rounds before quitting"""
    sys.path.insert(0, '.')
    if 'rps' in sys.modules:
        del sys.modules['rps']
    
    computer_choices = ['scissors', 'paper', 'rock']
    with patch('builtins.input', side_effect=['rock', 'scissors', 'paper', 'quit']):
        with patch('random.choice', side_effect=computer_choices):
            f = io.StringIO()
            with redirect_stdout(f):
                try:
                    import rps
                except (SystemExit, KeyboardInterrupt):
                    pass
            output = f.getvalue().lower()
            
            # Count occurrences of win/lose/tie messages (should be 3)
            win_count = output.count('win') + output.count('lose') + output.count('tie') + output.count('draw')
            if win_count < 3:
                raise check50.Failure(f"Expected program to handle multiple rounds, output:\n{f.getvalue()}")
