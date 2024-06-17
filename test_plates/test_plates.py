from plates import is_valid
import pytest
def main():
    test_isvalid1()
    test_isvalid2()
    test_isvalid3()


def test_isvalid1():
    assert is_valid("MN") == True
    assert is_valid("W5") == False
    assert is_valid("1J") == False
    # assert is_valid("11") == False
    # assert is_valid("a") == False
    # assert is_valid("A") == False

def test_isvalid2():
    assert is_valid("AA50800") == False
    assert is_valid("MA85") == True
    assert is_valid("AA.!") == False
    # assert is_valid("cs50!") == False
    # assert is_valid("cs 50") == False
    assert is_valid("BB05") == False


def test_isvalid3():
    assert is_valid("HELLO") == True
    assert is_valid("ABCDEFGHI") == False
    assert is_valid("AAA11A") == False

if __name__ == "__main__":
    main()
