import pytest

from app import addition

def test_addition():
    assert 4 == addition(2, 2)
    assert 100 == addition(70, 30)