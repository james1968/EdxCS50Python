from seasons import validate, get_days
import pytest


def test_validate_one_year():
    assert validate("2021-10-13") == True

def test_validate_two_year():
    assert validate("2020-10-13") == True

def test_validate_invalid():
    with pytest.raises(SystemExit):
        validate("2021-31-12")