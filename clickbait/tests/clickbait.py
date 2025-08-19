import check50
import re

@check50.check()
def exists():
    """clickbait.py exists"""
    check50.exists("clickbait.py")

@check50.check(exists)
def runs():
    """clickbait.py runs without syntax errors"""
    # Provide all 6 inputs: 3 headlines × 2 inputs each
    check50.run("python3 clickbait.py", 
                stdin="Alice\npickles\n7\ncats\nParis\nhaunted\n").exit(0)

@check50.check(runs)
def headline1_contains_inputs():
    """first headline contains both inputs"""
    inputs = ["Alice", "pickles"]
    output = check50.run("python3 clickbait.py", 
                         stdin="Alice\npickles\n7\ncats\nParis\nhaunted\n").stdout()
    for inp in inputs:
        if inp not in output:
            raise check50.Failure(f"'{inp}' not found in first headline output")

@check50.check(runs)
def headline2_contains_inputs():
    """second headline contains both inputs"""
    inputs = ["7", "cats"]
    output = check50.run("python3 clickbait.py", 
                         stdin="Alice\npickles\n7\ncats\nParis\nhaunted\n").stdout()
    for inp in inputs:
        if inp not in output:
            raise check50.Failure(f"'{inp}' not found in second headline output")

@check50.check(runs)
def headline3_contains_inputs():
    """third headline contains both inputs"""
    inputs = ["Paris", "haunted"]
    output = check50.run("python3 clickbait.py", 
                         stdin="Alice\npickles\n7\ncats\nParis\nhaunted\n").stdout()
    for inp in inputs:
        if inp not in output:
            raise check50.Failure(f"'{inp}' not found in third headline output")

@check50.check(runs)
def prompts_exactly_three_times():
    """program prompts the user exactly 3 times"""
    # Count how many times "Enter" appears in prompts
    output = check50.run("python3 clickbait.py", 
                         stdin="Alice\npickles\n7\ncats\nParis\nhaunted\n").stdout()
    prompt_count = len(re.findall(r"Enter", output))
    if prompt_count != 6:
        raise check50.Failure(f"expected 6 prompts (2 per headline), found {prompt_count}")
