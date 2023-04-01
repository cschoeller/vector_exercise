"""This module implements a simple vector class."""

class Vector:
    """Vector class supporting basic element-wise math operations."""

    def __init__(self, data):
        """Constructs the object.
        
        Args:
            data: List of values the vector contains.
        """
        self._data = data

    def __len__(self):
        """Returns the size of the vector."""
        return len(self._data)

    def __getitem__(self, idx):
        """Access value at specified index."""
        return self._data[idx]

    def __repr__(self):
        """Generates a readable string representation."""
        str_values = [str(x) for x in self._data]
        return "Vector([" + ",".join(str_values) + "])"

    def __add__(self, v):
        """Adds values of vector v element-wise."""
        new_data = []
        for i in range(len(v)):
            new_data.append(self._data[i] + v[i])
        return Vector(new_data)

    def __sub__(self, v):
        """Subtracts values of vector v element-wise."""
        new_data = []
        for i in range(len(v)):
            new_data.append(self._data[i] - v[i])
        return Vector(new_data)

    def __mul__(self, v):
        """Multiplies values of vector v element-wise."""
        new_data = []
        for i in range(len(v)):
            new_data.append(self._data[i] * v[i])
        return Vector(new_data)

    def __matmul__(self, v):
        """Dot product with vector v."""
        z = self * v
        return sum(z)

    def __truediv__(self, v):
        """Divides element-wise by values of vector v."""
        new_data = []
        for i in range(len(v)):
            new_data.append(self._data[i] / v[i])
        return Vector(new_data)

    def __pow__(self, p):
        """Takes values of vector to the given power."""
        new_data = [x**p for x in self._data]
        return Vector(new_data)

    def cat(self, v):
        """Concatenates this vector with vector v."""
        new_data = self._data + v._data
        return Vector(new_data)
