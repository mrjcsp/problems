import check50
import re

@check50.check()
def exists():
    """clickbait.py exists"""
    check50.exists("clickbait.py")

def run_program(inputs):
    """Helper to run clickbait.py with a list of inputs and capture output"""
    run = check50.run("python3 clickbait.py")
    for i in inputs:
        run = run.stdin(i)
    return run.stdout()

@check50.check(exists)
def headlines_contain_inputs():
    """Three headlines each contain their two inputs"""
    inputs_list = [
        ["Alice", "pickles"],
        ["7", "cats"],
        ["Paris", "haunted"]
    ]

    output = run_program([item for sublist in inputs_list for item in sublist])

    for inputs in inputs_list:
        for inp in inputs:
            if inp not in output:
                raise check50.Failure(f"'{inp}' not found in headline output")

@check50.check(exists)
def prompts_count():
    """Program prompts exactly 6 times (2 per headline)"""
    inputs = ["Alice", "pickles", "7", "cats", "Paris", "haunted"]
    output = run_program(inputs)
    prompt_count = len(re.findall(r"Enter", output))
    if prompt_count != 6:
        raise check50.Failure(f"expected 6 prompts (2 per headline), found {prompt_count}")
