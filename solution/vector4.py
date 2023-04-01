"""This module implements a simple vector class."""

from __future__ import annotations

from typing import Sequence, Union, Iterator

_NumericType = Union[int, float]


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

    def _check_equal_size(self, v: Vector) -> None:
        """Checks if vector sizes match."""
        if len(self) != len(v):
            raise ValueError("Vectors must be of equal size.")

    def _check_non_zero(self, v: Vector) -> None:
        """Checks if all values in vector are non-zero."""
        if not all([x != 0 for x in v]):
            raise ArithmeticError("Division by zero.")

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

    def __add__(self, v: Vector) -> Vector:
        """Adds values of vector v element-wise."""
        self._check_equal_size(v)
        new_data = []
        for i in range(len(v)):
            new_data.append(self._data[i] + v[i])
        return Vector(new_data)

    def __sub__(self, v: Vector) -> Vector:
        """Subtracts values of vector v element-wise."""
        self._check_equal_size(v)
        new_data = []
        for i in range(len(v)):
            new_data.append(self._data[i] - v[i])
        return Vector(new_data)

    def __mul__(self, v: Vector) -> Vector:
        """Multiplies values of vector v element-wise."""
        self._check_equal_size(v)
        new_data = []
        for i in range(len(v)):
            new_data.append(self._data[i] * v[i])
        return Vector(new_data)
    
    def __matmul__(self, v: Vector) -> _NumericType:
        """Dot product with vector v."""
        self._check_equal_size(v)
        z = self * v
        return sum(z)

    def __truediv__(self, v: Vector) -> Vector:
        """Divides element-wise by values of vector v."""
        self._check_equal_size(v)
        self._check_non_zero(v)
        new_data = []
        for i in range(len(v)):
            new_data.append(self._data[i] / v[i])
        return Vector(new_data)

    def __pow__(self, p: int) -> Vector:
        """Takes values of vector to the given power."""
        new_data = [x**p for x in self._data]
        return Vector(new_data)

    def cat(self, v: Vector) -> Vector:
        """Concatenates this vector with vector v."""
        new_data = self._data + v._data
        return Vector(new_data)
