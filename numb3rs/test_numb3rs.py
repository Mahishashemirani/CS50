import pytest
from numb3rs import validate

def test_correct():
    assert validate("1.2.3.4") == True
    assert validate("2.55.25.255") ==True

def test_wrong():
    assert validate ("555.60.111.798.210")== False
    assert validate ("646.56.4564.51")== False
    assert validate('Meow')  == False
    assert validate ('23.54.60') ==False
    assert validate("85.850.85.85") == False
