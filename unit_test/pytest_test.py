import pytest

from math_utils import *


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 1, 1),
    (1, 0, 1),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (0, 1, -1),
    (1, 0, 1),
    (0, 0, 0),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (0, 1, 0),
    (1, 0, 0),
    (0, 0, 0),
    (2, 3, 6)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (0, 1, 0),
    (1, 2, 0.5),
    (2, 2, 1),
    (10, 2, 5)
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_zero_divide():
    with pytest.raises(ValueError):
        divide(0, 0)
