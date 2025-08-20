import check50
import importlib

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
    student = importlib.import_module("pokemon")
    
    # Reset globals
    student.pokemon_level = 0
    student.pokemon_name = "Pichu"
    
    # Train 5 times -> should evolve to Stage 1
    for _ in range(5):
        student.pokemon_level += 1
        student.evolve_pokemon()
    if student.pokemon_level != 5:
        raise check50.Failure("pokemon_level did not increase correctly after training")
    if student.pokemon_name != "Pikachu":
        raise check50.Failure("Pokemon did not evolve to Stage 1 at level 5")
    
    # Train 5 more times -> should evolve to Stage 2
    for _ in range(5):
        student.pokemon_level += 1
        student.evolve_pokemon()
    if student.pokemon_level != 10:
        raise check50.Failure("pokemon_level did not increase correctly after training to level 10")
    if student.pokemon_name != "Raichu":
        raise check50.Failure("Pokemon did not evolve to Stage 2 at level 10")

@check50.check(exists)
def test_display():
    """Display function prints name and level"""
    student = importlib.import_module("pokemon")
    student.pokemon_level = 7
    student.pokemon_name = "Pikachu"
    output = student.display_pokemon()
    # Check that display prints something containing the name and level
    if not ("Pikachu" in str(output) or "7" in str(output)):
        raise check50.Failure("display_pokemon does not show correct name or level")
