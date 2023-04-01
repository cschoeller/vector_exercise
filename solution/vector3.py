"""This module implements a simple vector class."""

from __future__ import annotations
from typing import Union

_NumericType = Union[int, float]


class Vector:
    """Vector class supporting basic element-wise math operations."""

    def __init__(self, data: list[_NumericType]) -> None:
        """Constructs the object.
        
        Args:
            data: List of values the vector contains.
        """
        self._data = data

    def __len__(self) -> int:
        """Returns the size of the vector."""
        return len(self._data)

    def __getitem__(self, idx: int) -> _NumericType:
        """Access value at specified index."""
        return self._data[idx]

    def __repr__(self) -> str:
        """Generates a readable string representation."""
        str_values = [str(x) for x in self._data]
        return "Vector([" + ",".join(str_values) + "])"

    def __add__(self, v: Vector) -> Vector:
        """Adds values of vector v element-wise."""
        new_data = []
        for i in range(len(v)):
            new_data.append(self._data[i] + v[i])
        return Vector(new_data)

    def __sub__(self, v: Vector) -> Vector:
        """Subtracts values of vector v element-wise."""
        new_data = []
        for i in range(len(v)):
            new_data.append(self._data[i] - v[i])
        return Vector(new_data)

    def __mul__(self, v: Vector) -> Vector:
        """Multiplies values of vector v element-wise."""
        new_data = []
        for i in range(len(v)):
            new_data.append(self._data[i] * v[i])
        return Vector(new_data)
    
    def __matmul__(self, v: Vector) -> _NumericType:
        """Dot product with vector v."""
        z = self * v
        return sum(z)

    def __truediv__(self, v: Vector) -> Vector:
        """Divides element-wise by values of vector v."""
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
