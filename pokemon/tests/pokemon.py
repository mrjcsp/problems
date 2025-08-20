import check50

@check50.check()
def exists():
    """pokemon.py exists"""
    check50.exists("pokemon.py")

@check50.check(exists)
def globals_exist():
    """Defines pokemon_level and pokemon_name as global variables"""
    source = open("pokemon.py").read()
    for var in ["pokemon_level", "pokemon_name"]:
        if var not in source:
            raise check50.Failure(f"{var} not found in program")

@check50.check(exists)
def evolve_function_exists():
    """Defines evolve_pokemon function"""
    source = open("pokemon.py").read()
    if "def evolve_pokemon" not in source:
        raise check50.Failure("evolve_pokemon function not found")

@check50.check(exists)
def display_function_exists():
    """Defines display_pokemon function"""
    source = open("pokemon.py").read()
    if "def display_pokemon" not in source:
        raise check50.Failure("display_pokemon function not found")

@check50.check(exists)
def test_evolution_logic():
    """Checks that evolve_pokemon correctly evolves a Pokemon at level 5 and 10"""
    namespace = {}
    exec(open("pokemon.py").read(), namespace)

    # Test evolution at level 5
    namespace["pokemon_level"] = 5
    namespace["pokemon_name"] = "Pichu"
    namespace["evolve_pokemon"]()
    if namespace["pokemon_name"] != "Pikachu":
        raise check50.Failure("Pokemon should evolve to Pikachu at level 5")

    # Test evolution at level 10
    namespace["pokemon_level"] = 10
    namespace["pokemon_name"] = "Pikachu"
    namespace["evolve_pokemon"]()
    if namespace["pokemon_name"] != "Raichu":
        raise check50.Failure("Pokemon should evolve to Raichu at level 10")

@check50.check(exists)
def test_display_output():
    """Checks that display_pokemon prints the name and level"""
    namespace = {}
    exec(open("pokemon.py").read(), namespace)

    namespace["pokemon_name"] = "Pikachu"
    namespace["pokemon_level"] = 7

    output = str(namespace["display_pokemon"]())
    if "Pikachu" not in output or "7" not in output:
        raise check50.Failure("display_pokemon does not show correct name or level")
