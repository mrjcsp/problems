import check50
import re

@check50.check()
def exists():
    """clickbait.py exists"""
    check50.exists("clickbait.py")

@check50.check(exists)
def runs_and_contains_inputs():
    """Program runs, prints three headlines with correct inputs, and prompts six times"""
    
    # Provide all inputs at once
    run = check50.run("python3 clickbait.py") \
        .stdin("Alice") \
        .stdin("pickles") \
        .stdin("7") \
        .stdin("cats") \
        .stdin("Paris") \
        .stdin("haunted") \
        .stdout()

    # Check prompts
    prompt_count = len(re.findall(r"Enter", run))
    if prompt_count != 6:
        raise check50.Failure(f"expected 6 prompts, found {prompt_count}")

    # Check that each headline contains its inputs
    headlines_inputs = [
        ["Alice", "pickles"],
        ["7", "cats"],
        ["Paris", "haunted"]
    ]

    for inputs in headlines_inputs:
        for inp in inputs:
            if inp not in run:
                raise check50.Failure(f"'{inp}' not found in headline output")
