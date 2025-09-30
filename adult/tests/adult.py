import check50
import ast

def _load_function_from_source(filename: str, func_name: str):
    """
    Parse filename, extract the AST node for func_name (FunctionDef),
    compile and exec only that function into a fresh namespace, and
    return the namespace dict (with the function available).
    Raises descriptive exceptions on failure.
    """
    src = open(filename).read()
    tree = ast.parse(src, filename)
    # find function node
    func_node = None
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            func_node = node
            break
    if func_node is None:
        raise RuntimeError(f"Function '{func_name}' not found")

    # Create a new module containing only that function definition
    new_mod = ast.Module(body=[func_node], type_ignores=[])
    ast.fix_missing_locations(new_mod)
    code_obj = compile(new_mod, filename, "exec")
    namespace = {}
    exec(code_obj, namespace)
    if func_name not in namespace or not callable(namespace[func_name]):
        raise RuntimeError(f"Failed to load function '{func_name}'")
    return namespace

@check50.check()
def exists():
    """adult.py exists"""
    check50.exists("adult.py")

@check50.check(exists)
def function_defined():
    """Defines function is_adult(age)"""
    try:
        _load_function_from_source("adult.py", "is_adult")
    except Exception as e:
        raise check50.Failure(f"Function 'is_adult' not found or could not be loaded: {e}")

@check50.check(function_defined)
def returns_boolean_under_18():
    """is_adult(17) returns False (boolean)"""
    try:
        ns = _load_function_from_source("adult.py", "is_adult")
        result = ns
    except Exception as e:
        raise check50.Failure(f"Error calling is_adult(17): {e}")
    if not isinstance(result, bool):
        raise check50.Failure(f"is_adult(17) should return a boolean (True/False), not {type(result)}")
    if result is not False:
        raise check50.Failure("is_adult(17) should return False")

@check50.check(function_defined)
def returns_boolean_at_18():
    """is_adult(18) returns True (boolean)"""
    try:
        ns = _load_function_from_source("adult.py", "is_adult")
        result = ns
    except Exception as e:
        raise check50.Failure(f"Error calling is_adult(18): {e}")
    if not isinstance(result, bool):
        raise check50.Failure(f"is_adult(18) should return a boolean (True/False), not {type(result)}")
    if result is not True:
        raise check50.Failure("is_adult(18) should return True")

@check50.check(function_defined)
def returns_boolean_above_18():
    """is_adult(30) returns True (boolean)"""
    try:
        ns = _load_function_from_source("adult.py", "is_adult")
        result = ns
    except Exception as e:
        raise check50.Failure(f"Error calling is_adult(30): {e}")
    if not isinstance(result, bool):
        raise check50.Failure(f"is_adult(30) should return a boolean (True/False), not {type(result)}")
    if result is not True:
        raise check50.Failure("is_adult(30) should return True")
