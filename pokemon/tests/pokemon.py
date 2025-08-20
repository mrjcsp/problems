import check50

@check50.check()
def exists():
    """pokemon.py exists"""
    check50.exists("pokemon.py")

@check50.check(exists)
def globals_exist():
    """Program defines pokemon_level and pokemon_name as global variables"""
    source = open("pokemon.py").read()
    for var in ["pokemon_level", "pokemon_name"]:
        if var not in source:
            raise check50.Failure(f"{var} not found in program")

@check50.check(exists)
def evolve_function_exists():
    """Program defines evolve_pokemon function"""
    source = open("pokemon.py").read()
    if "def evolve_pokemon" not in source:
        raise check50.Failure("evolve_pokemon function not found")

@check50.check(exists)
def display_function_exists():
    """Program defines display_pokemon function"""
    source = open("pokemon.py").read()
    if "def display_pokemon" not in source:
        raise check50.Failure("display_pokemon function not found")

@check50.check(exists)
def test_training_and_evolution():
    """Training increases level and triggers evolutions correctly"""
    namespace = {}
    with open("pokemon.py") as f:
        code = f.read()
    exec(code, namespace)

    # Reset globals
    namespace["pokemon_level"] = 0
    namespace["pokemon_name"] = "Pichu"

    # Train 5 times -> evolve to Stage 1
    for _ in range(5):
        namespace["pokemon_level"] += 1
        namespace["evolve_pokemon"]()
    if namespace["pokemon_level"] != 5:
        raise check50.Failure("pokemon_level did not increase correctly after training")
    if namespace["pokemon_name"] != "Pikachu":
        raise check50.Failure("Pokemon did not evolve to Stage 1 at level 5")

    # Train 5 more times -> evolve to Stage 2
    for _ in range(5):
        namespace["pokemon_level"] += 1
        namespace["evolve_pokemon"]()
    if namespace["pokemon_level"] != 10:
        raise check50.Failure("pokemon_level did not increase correctly after training to level 10")
    if namespace["pokemon_name"] != "Raichu":
        raise check50.Failure("Pokemon did not evolve to Stage 2 at level 10")

@check50.check(exists)
def test_display():
    """Display function prints name and level"""
    namespace = {}
    with open("pokemon.py") as f:
        code = f.read()
    exec(code, namespace)

    namespace["pokemon_level"] = 7
    namespace["pokemon_name"] = "Pikachu"

    output = namespace["display_pokemon"]()
    # Check that display prints something containing the name and level
    if not ("Pikachu" in str(output) or "7" in str(output)):
        raise check50.Failure("display_pokemon does not show correct name or level")
