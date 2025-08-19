import check50
import ast

@check50.check()
def exists():
    """clickbait.py exists"""
    check50.exists("clickbait.py")

@check50.check(exists)
def functions_exist():
    """clickbait.py defines the required functions"""
    with open("clickbait.py") as f:
        tree = ast.parse(f.read(), filename="clickbait.py")
    
    # Collect all function names
    func_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    
    required_funcs = ["headline1", "headline2", "headline3"]
    
    for func in required_funcs:
        if func not in func_names:
            raise check50.Failure(f"Function '{func}' not found in clickbait.py")

@check50.check(functions_exist)
def headlines_contain_inputs():
    """Program prints three headlines containing the correct inputs"""
    
    # Provide all inputs at once (2 per headline)
    inputs = "Alice\npickles\n7\ncats\nParis\nhaunted\n"

    # Run the program
    output = check50.run("python3 clickbait.py").stdin(inputs).stdout()

    # Each headline has its two inputs
    headlines_inputs = [
        ["Alice", "pickles"],
        ["7", "cats"],
        ["Paris", "haunted"]
    ]

    # Check that each input appears somewhere in the output
    for pair in headlines_inputs:
        for inp in pair:
            if inp not in output:
                raise check50.Failure(f"'{inp}' not found in headline output")
