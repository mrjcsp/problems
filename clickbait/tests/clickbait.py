import check50
import re

@check50.check()
def exists():
    """clickbait.py exists"""
    check50.exists("clickbait.py")

@check50.check(exists)
def runs():
    """clickbait.py runs without syntax errors"""
    check50.run("python3 clickbait.py") \
        .stdin("Alice") \
        .stdin("pickles") \
        .stdin("7") \
        .stdin("cats") \
        .stdin("Paris") \
        .stdin("haunted") \
        .exit(0)

def run_with_inputs():
    """helper function to run clickbait.py with all inputs and return output"""
    return check50.run("python3 clickbait.py") \
        .stdin("Alice") \
        .stdin("pickles") \
        .stdin("7") \
        .stdin("cats") \
        .stdin("Paris") \
        .stdin("haunted") \
        .stdout()

@check50.check(runs)
def headline1_contains_inputs():
    """first headline contains both inputs"""
    output = run_with_inputs()
    inputs = ["Alice", "pickles"]
    for inp in inputs:
        if inp not in output:
            raise check50.Failure(f"'{inp}' not found in first headline output")

@check50.check(runs)
def headline2_contains_inputs():
    """second headline contains both inputs"""
    output = run_with_inputs()
    inputs = ["7", "cats"]
    for inp in inputs:
        if inp not in output:
            raise check50.Failure(f"'{inp}' not found in second headline output")

@check50.check(runs)
def headline3_contains_inputs():
    """third headline contains both inputs"""
    output = run_with_inputs()
    inputs = ["Paris", "haunted"]
    for inp in inputs:
        if inp not in output:
            raise check50.Failure(f"'{inp}' not found in third headline output")

@check50.check(runs)
def prompts_exactly_six_times():
    """program prompts the user exactly 6 times (2 per headline)"""
    output = run_with_inputs()
    prompt_count = len(re.findall(r"Enter", output))
    if prompt_count != 6:
        raise check50.Failure(f"expected 6 prompts (2 per headline), found {prompt_count}")
