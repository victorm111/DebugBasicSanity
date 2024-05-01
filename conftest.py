"""
Basic conftest.py file
can include global access fixtures

Args:
    param1: n/a

Returns:
    global access fixtures

Raises:
    tbd, added as required in future
"""
import pytest


@pytest.fixture()
def fixture():
    return "some stuff"




