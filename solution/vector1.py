class Vector:

    def __init__(self, data):
        self._data = data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, idx):
        return self._data[idx]

    def __repr__(self):
        str_values = [str(x) for x in self._data]
        return "Vector([" + ",".join(str_values) + "])"

    def __add__(self, v):
        new_data = []
        for i in range(len(v)):
            new_data.append(self._data[i] + v[i])
        return Vector(new_data)

    def __sub__(self, v):
        new_data = []
        for i in range(len(v)):
            new_data.append(self._data[i] - v[i])
        return Vector(new_data)

    def __mul__(self, v):
        new_data = []
        for i in range(len(v)):
            new_data.append(self._data[i] * v[i])
        return Vector(new_data)

    def __matmul__(self, v):
        z = self * v
        return sum(z)

    def __truediv__(self, v):
        new_data = []
        for i in range(len(v)):
            new_data.append(self._data[i] / v[i])
        return Vector(new_data)

    def __pow__(self, p):
        new_data = [x**p for x in self._data]
        return Vector(new_data)

    def cat(self, v):
        new_data = self._data + v._data
        return Vector(new_data)