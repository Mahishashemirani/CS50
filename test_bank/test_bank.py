from bank import value
import pytest
def test_bank():
    assert value("hello") == 0
    assert value("HeLLo") == 0
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("What's up") == 100
    assert value("What a Day!") == 100
    assert value("Welcome!") == 100

