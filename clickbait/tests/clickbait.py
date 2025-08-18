import check50

@check50.check()
def exists():
    """clickbait.py exists"""
    check50.exists("clickbait.py")

@check50.check(exists)
def runs():
    """clickbait.py runs without syntax errors"""
    check50.run("python3 clickbait.py").exit()

@check50.check(runs)
def test_headline1():
    """first headline contains both inputs"""
    out = (
        check50.run("python3 clickbait.py")
        .stdin("Beyonce")
        .stdin("pickles")
        .stdout()
    )
    if "Beyonce" not in out or "pickles" not in out:
        raise check50.Failure("Expected both 'Beyonce' and 'pickles' in the headline")

@check50.check(runs)
def test_headline2():
    """second headline contains both inputs"""
    out = (
        check50.run("python3 clickbait.py")
        .stdin("7")
        .stdin("cats")
        .stdout()
    )
    if "7" not in out or "cats" not in out:
        raise check50.Failure("Expected both '7' and 'cats' in the headline")

@check50.check(runs)
def test_headline3():
    """third headline contains both inputs"""
    out = (
        check50.run("python3 clickbait.py")
        .stdin("Paris")
        .stdin("haunted")
        .stdout()
    )
    if "Paris" not in out or "haunted" not in out:
        raise check50.Failure("Expected both 'Paris' and 'haunted' in the headline")

@check50.check(runs)
def prompts_exactly_three():
    """program prompts the user exactly 3 times"""
    run = check50.run("python3 clickbait.py")
    out = (
        run.stdin("test1")
        .stdin("test2")
        .stdin("test3")
        .stdin("test4")
        .stdin("test5")
        .stdin("test6")
        .stdout()
    )
    prompts = sum(phrase in out for phrase in ["Enter", "enter", "Input", "input"])
    if prompts != 3:
        raise check50.Failure(f"Expected exactly 3 input prompts, but found {prompts}")
