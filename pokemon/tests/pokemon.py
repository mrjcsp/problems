import check50

@check50.check()
def exists():
    """pokemon.py exists"""
    check50.exists("pokemon.py")

@check50.check(exists)
def global_variables():
    """Program defines pokemon_level and pokemon_name as global variables"""
    source = open("pokemon.py").read()
    for var in ["pokemon_level", "pokemon_name"]:
        if var not in source:
            raise check50.Failure(f"{var} not found in program")

@check50.check(exists)
def evolve_function():
    """Program defines evolve_pokemon function"""
    source = open("pokemon.py").read()
    if "def evolve_pokemon(" not in source:
        raise check50.Failure("evolve_pokemon function not defined")

@check50.check(exists)
def display_function():
    """Program defines display_pokemon function"""
    source = open("pokemon.py").read()
    if "def display_pokemon(" not in source:
        raise check50.Failure("display_pokemon function not defined")

@check50.check(exists)
def level_up_training():
    """Training increases pokemon_level by 1"""
    # Simulate training input
    output = check50.run("python3 pokemon.py").stdin("1\n5\n3\n").stdout()
    # Should contain increased level
    if "6" not in output and "level: 6" not in output:
        raise check50.Failure("pokemon_level did not increase by 1 after training")

@check50.check(exists)
def display_info():
    """Display function prints pokemon name and level"""
    output = check50.run("python3 pokemon.py").stdin("3\n").stdout()
    if "pokemon_name" not in output and "level" not in output:
        raise check50.Failure("display_pokemon did not show name or level")
