"""
NeuroForge Tensor

Author: Krishna Agrawal
"""


class Tensor:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Tensor({self.data})"

    def __add__(self, other):

        result = []

        for i in range(len(self.data)):
            result.append(self.data[i] + other.data[i])

        return Tensor(result)