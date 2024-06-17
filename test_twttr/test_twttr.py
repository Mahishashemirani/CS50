from twttr import shorten
import pytest
def test_twttr():
    assert shorten("enter") == "ntr"
    assert shorten("tElEgram") == "tlgrm"
    assert shorten ("123") == "123"
    assert shorten (".?!,") == ".?!,"



