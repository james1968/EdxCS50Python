from bank import value

def test_hello():
    assert value("hello") == 0

def test_hello2():
    assert value("Hello") == 0

def test_hello2():
    assert value("Hello, Newman") == 0

def test_h():
    assert value("h") == 20

def test_h2():
    assert value("H") == 20

def test_not_h():
    assert value("whats up") == 100

def test_not_h2():
    assert value(" whats up ") == 100

def test_number():
    assert value("0") == 100
