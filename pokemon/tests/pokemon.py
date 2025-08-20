import check50
import re

@check50.check()
def exists():
    """pokemon.py exists"""
    check50.exists("pokemon.py")

@check50.check(exists)
def globals_defined():
    """Program defines global variables pokemon_level and pokemon_name"""
    source = check50.read("pokemon.py")
    if "pokemon_level" not in source:
        raise check50.Failure("Global variable 'pokemon_level' not found")
    if "pokemon_name" not in source:
        raise check50.Failure("Global variable 'pokemon_name' not found")

@check50.check(exists)
def train_defined():
    """Program defines a train function"""
    source = check50.read("pokemon.py")
    if not re.search(r"def\s+train\s*\(", source):
        raise check50.Failure("Function 'train' not found")

@check50.check(exists)
def evolve_defined():
    """Program defines an evolve_pokemon function"""
    source = check50.read("pokemon.py")
    if not re.search(r"def\s+evolve_pokemon\s*\(", source):
        raise check50.Failure("Function 'evolve_pokemon' not found")

@check50.check(exists)
def display_defined():
    """Program defines a display_pokemon function"""
    source = check50.read("pokemon.py")
    if not re.search(r"def\s+display_pokemon\s*\(", source):
        raise check50.Failure("Function 'display_pokemon' not found")
