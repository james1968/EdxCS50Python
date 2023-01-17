from numb3rs import validate

def test_success_1():
    assert validate(r"255.255.255.255") == True

def test_success_2():
    assert validate(r"0.0.0.0") == True

def test_success_3():
    assert validate(r"1.22.255.1") == True

def test_fail_too_large():
    assert validate(r"512.1.1.1") == False
    assert validate(r"1.512.1.1") == False
    assert validate(r"1.1.512.1") == False
    assert validate(r"1.1.1.512") == False

def test_fail_non_numeric():
    assert validate(r"cat") == False

def test_fail_1():
    assert validate(r"1") == False
    assert validate(r"1.1") == False
    assert validate(r"1.1.1") == False