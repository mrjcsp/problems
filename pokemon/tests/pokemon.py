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

