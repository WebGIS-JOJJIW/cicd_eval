import pytest

from app import addition, subtraction

def test_addition():
    assert 4 == addition(2, 2)
    assert 100 == addition(70, 30)

def test_subtraction():
    assert 50 == subtraction(500, 450)
    assert 300 == subtraction(821, 521)
