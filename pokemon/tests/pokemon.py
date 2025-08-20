import check50
import inspect

@check50.check()
def exists():
    """pokemon.py exists"""
    check50.exists("pokemon.py")

@check50.check(exists)
def globals_defined():
    """Program defines global variables pokemon_level and pokemon_name"""
    import pokemon
    if not hasattr(pokemon, "pokemon_level"):
        raise check50.Failure("Global variable 'pokemon_level' is not defined")
    if not hasattr(pokemon, "pokemon_name"):
        raise check50.Failure("Global variable 'pokemon_name' is not defined")

@check50.check(exists)
def train_defined():
    """Program defines a train function"""
    import pokemon
    if not hasattr(pokemon, "train") or not inspect.isfunction(pokemon.train):
        raise check50.Failure("Function 'train' is not defined")

@check50.check(exists)
def evolve_defined():
    """Program defines an evolve_pokemon function"""
    import pokemon
    if not hasattr(pokemon, "evolve_pokemon") or not inspect.isfunction(pokemon.evolve_pokemon):
        raise check50.Failure("Function 'evolve_pokemon' is not defined")

@check50.check(exists)
def display_defined():
    """Program defines a display_pokemon function"""
    import pokemon
    if not hasattr(pokemon, "display_pokemon") or not inspect.isfunction(pokemon.display_pokemon):
        raise check50.Failure("Function 'display_pokemon' is not defined")
