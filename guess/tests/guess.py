import check50

@check50.check()
def exists():
    """guess.py exists"""
    check50.exists("guess.py")


@check50.check(exists)
def correct_guess():
    """Program congratulates user when guess is correct"""
    # Run the student's program and simulate input
    output = (
        check50.run("python3 guess.py")
        .stdin("5")     # Student guesses 5
        .stdout(timeout=5)
        .lower()
    )
    if "congrat" not in output:
        raise check50.Failure("Program did not congratulate the user on correct guess")


@check50.check(exists)
def incorrect_guess():
    """Program reveals secret number when guess is wrong"""
    output = (
        check50.run("python3 guess.py")
        .stdin("3")     # Student guesses wrong
        .stdout(timeout=5)
        .lower()
    )
    if "3" in output and "congrat" in output:
        raise check50.Failure("Incorrect guess should not congratulate")
    if "number" not in output and "was" not in output:
        raise check50.Failure("Program did not reveal the correct number when guess was wrong")
