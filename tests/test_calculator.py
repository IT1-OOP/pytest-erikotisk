import pytest
from src import calculator


def test_add():
    assert calculator.add(5,3) == 8