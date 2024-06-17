import pytest
from working import convert

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 6:00 PM") == "09:00 to 18:00"
    assert convert("9:00 PM to 4:00 AM") == "21:00 to 04:00"

    with pytest.raises(ValueError):
        assert convert("9:00 AM cat 7:31 PM")


    with pytest.raises(ValueError):
        assert convert("9:00 AM to 85:30 PM")
