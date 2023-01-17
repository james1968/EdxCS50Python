from um import count

def test_um():
    assert count("um?") == 1

def test_um1():
    assert count("Um, thanks, um...") == 2

def test_um2():
    assert count("Um, thanks for the album.") == 1
