import check50

@check50.check()
def exists():
    """bottles.py exists"""
    check50.exists("bottles.py")

@check50.check(exists)
def first_verse():
    """Program prints the first verse correctly"""
    output = check50.run("python3 bottles.py").stdout()
    expected = "99 bottles of milk on the wall, 99 bottles of milk."
    if expected not in output:
        raise check50.Failure("First verse not found or formatted incorrectly")

@check50.check(exists)
def last_verse():
    """Program prints the last verse correctly with singular 'bottle'"""
    output = check50.run("python3 bottles.py").stdout()
    expected = "1 bottle of milk on the wall, 1 bottle of milk."
    if expected not in output:
        raise check50.Failure("Last verse with singular 'bottle' not found or formatted incorrectly")

@check50.check(exists)
def no_more_bottles():
    """Program prints 'No more bottles of milk on the wall.' at the end"""
    output = check50.run("python3 bottles.py").stdout()
    expected = "No more bottles of milk on the wall."
    if expected not in output:
        raise check50.Failure("Final line 'No more bottles of milk on the wall.' not found")
