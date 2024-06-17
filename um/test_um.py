import pytest
from um import count

def test_all_cases_count():
    assert count("um um umberella UM") == 3
