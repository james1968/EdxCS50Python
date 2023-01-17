from plates import is_valid

def test_default():
    assert is_valid("CS50") == True

def test_fail10():
    assert is_valid(" ") == False

def test_pass():
    assert is_valid("AAA222") == True

def test_fail():
    assert is_valid("CS05") == False

def test_fail1():
    assert is_valid("CS50P") == False

def test_fail2():
    assert is_valid("CS50P") == False

def test_fail3():
    assert is_valid("50") == False

def test_fail4():
    assert is_valid("AAA2222") == False

def test_fail5():
    assert is_valid("AAA22A") == False

def test_fail6():
    assert is_valid("?!AAA") == False

def test_fail7():
    assert is_valid("AAAAAA") == True

def test_fail8():
    assert is_valid("123456") == False

def test_fail9():
    assert is_valid("CS") == True

def test_fail10():
    assert is_valid(" ") == False

def test_fail11():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False
    assert is_valid("PI 14") == False
