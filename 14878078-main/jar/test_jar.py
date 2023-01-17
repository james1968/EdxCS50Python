from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar1 = Jar(5)
    assert jar1.capacity == 5


def test_str():
    jar2 = Jar()
    assert str(jar2) == ""
    jar2.deposit(1)
    assert str(jar2) == "🍪"
    jar2.deposit(11)
    assert str(jar2) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar3 = Jar()
    jar3.deposit(5)
    assert jar3.size == 5
    jar3.deposit(2)
    assert jar3.size == 7


def test_withdraw():
    jar4 = Jar()
    jar4.deposit(5)
    jar4.withdraw(3)
    assert jar4.size == 2
    jar4.withdraw(1)
    assert jar4.size == 1