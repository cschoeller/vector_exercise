"""Tests for the vector class."""
# pylint: disable=invalid-name

from typing import Final

import pytest

from solution.vector5 import Vector


_DATA_A: Final = [1.2, 4.8, -3.1]
_DATA_B: Final = [5, 7.4, 0.6]


@pytest.fixture(name="vec_a")
def fxt_vector_a() -> Vector:
    """Vector fixture."""
    return Vector(_DATA_A)


@pytest.fixture(name="vec_b")
def fxt_vector_b() -> Vector:
    """Vector fixture."""
    return Vector(_DATA_B)


def test_vector_smoke_test() -> None:
    """Smoke test for the vector class."""
    data = [1.3, 0.7, 3.8]
    vec = Vector(data)
    assert vec[1] == 0.7
    for i, x in enumerate(vec):
        assert x == data[i]
    print(vec)

    with pytest.raises(ValueError):  # non-empty
        _ = Vector([])


def test_vector_add(vec_a: Vector, vec_b: Vector) -> None:
    """Test addition of vectors."""
    new_vec = vec_a + vec_b
    new_data = [x + y for x, y in zip(_DATA_A, _DATA_B)]
    for x, y in zip(new_vec, new_data):
        assert x == y

    with pytest.raises(ValueError):  # unequal length
        new_vec = vec_a + Vector([1.0, 1.0])


def test_vector_sub(vec_a: Vector, vec_b: Vector) -> None:
    """Test subtraction of vectors."""
    new_vec = vec_a - vec_b
    new_data = [x - y for x, y in zip(_DATA_A, _DATA_B)]
    for x, y in zip(new_vec, new_data):
        assert x == y

    with pytest.raises(ValueError):  # unequal length
        new_vec = vec_a - Vector([1.0, 1.0])


def test_vector_mul(vec_a: Vector, vec_b: Vector) -> None:
    """Test multiplication of vector."""
    new_vec = vec_a * vec_b
    new_data = [x * y for x, y in zip(_DATA_A, _DATA_B)]
    for x, y in zip(new_vec, new_data):
        assert x == y

    # scalar case
    scalar = -0.3
    new_vec = vec_a * scalar
    for x, y in zip(new_vec, vec_a):
        assert x == (y * scalar)

    with pytest.raises(ValueError):  # unequal length
        new_vec = vec_a * Vector([1.0, 1.0])


def test_vector_div(vec_a: Vector, vec_b: Vector) -> None:
    """Test division of vector."""
    new_vec = vec_a / vec_b
    new_data = [x / y for x, y in zip(_DATA_A, _DATA_B)]
    for x, y in zip(new_vec, new_data):
        assert x == y

    # scalar case
    scalar = 1.7
    new_vec = vec_a / scalar
    for x, y in zip(new_vec, vec_a):
        assert x == (y / scalar)

    with pytest.raises(ValueError):  # unequal length
        new_vec = vec_a / Vector([1.0, 1.0])

    with pytest.raises(ArithmeticError):  # zero divison
        new_vec = vec_a / Vector([0.0, 5.7, 0.1])

    with pytest.raises(ArithmeticError):  # zero divison
        new_vec = vec_a / 0.0


def test_vector_dot(vec_a: Vector, vec_b: Vector) -> None:
    """Test the dot product between two vectors"""
    dot_vec = vec_a @ vec_b
    dot_data = sum(x * y for x, y in zip(_DATA_A, _DATA_B))
    assert isinstance(dot_vec, float)
    assert dot_vec == dot_data

    with pytest.raises(ValueError):  # unequal length
        _ = vec_a @ Vector([1.0, 1.0])


def test_vector_pow(vec_a: Vector) -> None:
    """Test raising vector to power."""
    power = 3
    new_vec = vec_a**power
    for v, x in zip(new_vec, vec_a):
        assert v == (x**power)


def test_vector_cat(vec_a: Vector, vec_b: Vector) -> None:
    """Test vector concatenation."""
    cat_vec = vec_a.cat(vec_b)
    cat_data = _DATA_A + _DATA_B
    assert len(cat_data) == len(cat_vec)
    for x, y in zip(cat_data, cat_vec):
        assert x == y
