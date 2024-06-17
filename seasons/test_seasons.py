import pytest
from seasons import minutes

def test():
    assert minutes("2003-06-20") == "Eleven million, forty thousand, four hundred eighty minutes"
    with pytest.raises(SystemExit, match="Invalid"):
        minutes("Januar 6th, 1998")



test()
