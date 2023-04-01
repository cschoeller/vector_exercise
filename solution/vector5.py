"""This module implements a simple vector class."""
# pylint: disable=invalid-name

from __future__ import annotations

from typing import Callable, Iterator, Union

# type aliases
_NumericType = Union[int, float]
_OpType = Callable[[_NumericType, _NumericType], _NumericType]


def _add_op(x: _NumericType, y: _NumericType) -> _NumericType:
    """Adds two numeric values."""
    return x + y


def _sub_op(x: _NumericType, y: _NumericType) -> _NumericType:
    """Subtracts two numeric values."""
    return x - y


def _mul_op(x: _NumericType, y: _NumericType) -> _NumericType:
    """Multiplies two numeric values."""
    return x * y


def _div_op(x: _NumericType, y: _NumericType) -> _NumericType:
    """Divides two numeric values."""
    return x / y


class Vector:
    """Vector class supporting basic element-wise math operations."""

    def __init__(self, data: list[_NumericType]) -> None:
        """Constructs the object.

        Args:
            data: List of values the vector contains.
        """
        if len(data) == 0:
            raise ValueError("Data must be non-empty.")
        self._data = data

    def _check_equal_size(self, other: Vector) -> None:
        """Checks if vector sizes match."""
        if len(self) != len(other):
            raise ValueError("Vectors must be of equal size.")

    def _check_non_zero(self, other: Union[Vector, _NumericType]) -> None:
        """Checks if all values in vector are non-zero."""
        division_error = ArithmeticError("Division by zero.")
        if isinstance(other, Vector) and any(x == 0 for x in other):
            raise division_error
        if type(other) in (int, float) and other == 0:
            raise division_error

    def __len__(self) -> int:
        """Returns the size of the vector."""
        return len(self._data)

    def __getitem__(self, idx: int) -> _NumericType:
        """Access value at specified index."""
        return self._data[idx]

    def __iter__(self) -> Iterator:
        """Returns an iterator over values."""
        return iter(self._data)

    def __repr__(self) -> str:
        """Generates a readable string representation."""
        str_values = [str(x) for x in self._data]
        return "Vector([" + ",".join(str_values) + "])"

    def _apply_bivariate_op(self, other: Vector, op: _OpType) -> Vector:
        """Applies provided bivariate operation element-wise.

        Args:
            other: Vector to apply element-wise operation with.
            op: Pointer to function performing scalar operation.

        Returns:
            New vector resulting from applied operation.
        """
        return Vector([op(x, y) for x, y in zip(self._data, other)])

    def __add__(self, other: Vector) -> Vector:
        """Adds values of vector v element-wise."""
        self._check_equal_size(other)
        return self._apply_bivariate_op(other, _add_op)

    def __sub__(self, other: Vector) -> Vector:
        """Subtracts values of vector v element-wise."""
        self._check_equal_size(other)
        return self._apply_bivariate_op(other, _sub_op)

    def __mul__(self, other: Union[Vector, _NumericType]) -> Vector:
        """Multiplies element-wise with vector or scalar."""
        if isinstance(other, Vector):
            self._check_equal_size(other)
            return self._apply_bivariate_op(other, _mul_op)
        return Vector([_mul_op(x, other) for x in self._data])

    def __matmul__(self, other: Vector) -> _NumericType:
        """Dot product with vector."""
        self._check_equal_size(other)
        return sum(self * other)

    def __truediv__(self, other: Union[Vector, _NumericType]) -> Vector:
        """Divides element-wise by values vector or scalar."""
        self._check_non_zero(other)
        if isinstance(other, Vector):
            self._check_equal_size(other)
            return self._apply_bivariate_op(other, _div_op)
        return Vector([_div_op(x, other) for x in self._data])

    def __pow__(self, power: int) -> Vector:
        """Takes values of vector to the given power."""
        return Vector([x**power for x in self._data])

    def cat(self, other: Vector) -> Vector:
        """Concatenates this vector with vector other."""
        return Vector(self._data + other._data)  # pylint: disable=protected-access
