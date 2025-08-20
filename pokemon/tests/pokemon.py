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
def train_and_evolve():
    """Checks that training increases level by 1 and evolves at level 10"""
    namespace = {}
    exec(open("pokemon.py").read(), namespace)

    # Reset globals
    namespace["pokemon_level"] = 0
    namespace["pokemon_name"] = "Pichu"

    # Simulate 10 trainings
    for i in range(10):
        namespace["pokemon_level"] += 1
        namespace["evolve_pokemon"]()

    if namespace["pokemon_level"] != 10:
        raise check50.Failure("Training did not increase pokemon_level correctly")

    if namespace["pokemon_name"] != "Raichu":
        raise check50.Failure("Pokemon should evolve to Raichu after 10 trainings")
