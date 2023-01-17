from twttr import shorten


def test_default():
    assert shorten("hello") == "hll"

def test_random():
    assert shorten("rt56euiklm") == "rt56klm"

def test_capitalised_vowel():
    assert shorten("Hello") == "Hll"

def test_punctuation():
    assert shorten("hEll") == "hll"

def test_punctuation():
    assert shorten("h.E?ll") == "h.?ll"

