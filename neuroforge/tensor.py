"""
NeuroForge Tensor

Author: Krishna Agrawal
"""


class Tensor:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Tensor({self.data})"

    # Addition
    def __add__(self, other):

        result = []

        for i in range(len(self.data)):
            result.append(self.data[i] + other.data[i])

        return Tensor(result)

    # Subtraction
    def __sub__(self, other):

        result = []

        for i in range(len(self.data)):
            result.append(self.data[i] - other.data[i])

        return Tensor(result)

    # Multiplication
    def __mul__(self, other):

        result = []

        for i in range(len(self.data)):
            result.append(self.data[i] * other.data[i])

        return Tensor(result)

    # Division
    def __truediv__(self, other):

        result = []

        for i in range(len(self.data)):
            result.append(self.data[i] / other.data[i])

        return Tensor(result)