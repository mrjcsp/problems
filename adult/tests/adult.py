import check50

@check50.check()
def exists():
    """adult.py exists"""
    check50.exists("adult.py")

@check50.check(exists)
def imports():
    """adult.py can be imported"""
    check50.py.import_("adult.py")

@check50.check(imports)
def test_exactly_18():
    """is_adult(18) returns True"""
    adult = check50.py.import_("adult.py")
    result = adult.is_adult(18)
    if result != True:
        raise check50.Failure(f"Expected True, got {result}")

@check50.check(imports)
def test_over_18():
    """is_adult(25) returns True"""
    adult = check50.py.import_("adult.py")
    result = adult.is_adult(25)
    if result != True:
        raise check50.Failure(f"Expected True, got {result}")

@check50.check(imports)
def test_under_18():
    """is_adult(17) returns False"""
    adult = check50.py.import_("adult.py")
    result = adult.is_adult(17)
    if result != False:
        raise check50.Failure(f"Expected False, got {result}")

@check50.check(imports)
def test_zero():
    """is_adult(0) returns False"""
    adult = check50.py.import_("adult.py")
    result = adult.is_adult(0)
    if result != False:
        raise check50.Failure(f"Expected False, got {result}")

@check50.check(imports)
def test_very_young():
    """is_adult(5) returns False"""
    adult = check50.py.import_("adult.py")
    result = adult.is_adult(5)
    if result != False:
        raise check50.Failure(f"Expected False, got {result}")

@check50.check(imports)
def test_elderly():
    """is_adult(100) returns True"""
    adult = check50.py.import_("adult.py")
    result = adult.is_adult(100)
    if result != True:
        raise check50.Failure(f"Expected True, got {result}")

@check50.check(imports)
def test_just_under_18():
    """is_adult(17.9) returns False"""
    adult = check50.py.import_("adult.py")
    result = adult.is_adult(17.9)
    if result != False:
        raise check50.Failure(f"Expected False, got {result}")
