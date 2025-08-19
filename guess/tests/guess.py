import check50
import random

@check50.check()
def exists():
    """guess.py exists"""
    check50.exists("guess.py")


@check50.check(exists)
def correct_guess():
    """Program congratulates user when guess is correct"""
    # Force secret number to 5 by patching random.randint
    output = (
        check50.run("python3 -c \"import random; random.randint=lambda a,b: 5; import guess\"")
        .stdin("5")
        .stdout()
        .lower()
    )
    if "congrat" not in output:
        raise check50.Failure("Program did not congratulate the user on correct guess")


@check50.check(exists)
def incorrect_guess():
    """Program reveals secret number when guess is wrong"""
    # Force secret number to 7
    output = (
        check50.run("python3 -c \"import random; random.randint=lambda a,b: 7; import guess\"")
        .stdin("3")
        .stdout()
        .lower()
    )
    if "7" not in output:
        raise check50.Failure("Program did not reveal the correct number when guess was wrong")
