from working import convert
import pytest

def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")

def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5 PM")


def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"


def test_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")


def test_format():
    with pytest.raises(ValueError):
        convert("9 to 5")
    with pytest.raises(ValueError):
        convert("17:00 to 9 PM")

def test_correct():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_incorrect():
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:60 PM")
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 17 PM")

def test_incorrect2():
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")

def test_incorrect3():
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:60 PM")


