import check50
import ast

@check50.check()
def exists():
    """clickbait.py exists"""
    check50.exists("clickbait.py")

@check50.check(exists)
def headline1_exists():
    """clickbait.py defines the function headline1"""
    with open("clickbait.py") as f:
        tree = ast.parse(f.read(), filename="clickbait.py")
    func_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    if "headline1" not in func_names:
        raise check50.Failure("Function 'headline1' not found in clickbait.py")

@check50.check(exists)
def headline2_exists():
    """clickbait.py defines the function headline2"""
    with open("clickbait.py") as f:
        tree = ast.parse(f.read(), filename="clickbait.py")
    func_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    if "headline2" not in func_names:
        raise check50.Failure("Function 'headline2' not found in clickbait.py")

@check50.check(exists)
def headline3_exists():
    """clickbait.py defines the function headline3"""
    with open("clickbait.py") as f:
        tree = ast.parse(f.read(), filename="clickbait.py")
    func_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    if "headline3" not in func_names:
        raise check50.Failure("Function 'headline3' not found in clickbait.py")

@check50.check([headline1_exists, headline2_exists, headline3_exists])
def headline1_output():
    """First headline prints both inputs"""
    inputs = "Alice\npickles\n7\ncats\nParis\nhaunted\n"
    output = check50.run("python3 clickbait.py").stdin(inputs).stdout()
    if "Alice" not in output or "pickles" not in output:
        raise check50.Failure("First headline does not contain both inputs")

@check50.check([headline1_exists, headline2_exists, headline3_exists])
def headline2_output():
    """Second headline prints both inputs"""
    inputs = "Alice\npickles\n7\ncats\nParis\nhaunted\n"
    output = check50.run("python3 clickbait.py").stdin(inputs).stdout()
    if "7" not in output or "cats" not in output:
        raise check50.Failure("Second headline does not contain both inputs")

@check50.check([headline1_exists, headline2_exists, headline3_exists])
def headline3_output():
    """Third headline prints both inputs"""
    inputs = "Alice\npickles\n7\ncats\nParis\nhaunted\n"
    output = check50.run("python3 clickbait.py").stdin(inputs).stdout()
    if "Paris" not in output or "haunted" not in output:
        raise check50.Failure("Third headline does not contain both inputs")
