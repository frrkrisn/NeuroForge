"""
NeuroForge Tensor

Author: Krishna Agrawal
"""


class Tensor:

    def __init__(self, data):
        self.data = data

        self.shape = self._get_shape(data)

    def __repr__(self):
        return f"Tensor({self.data})"

    def _validate(self, other):
        """
        Validate that two tensors have the same size.
        """

        if len(self.data) != len(other.data):
            raise ValueError(
                f"Tensor size mismatch: {len(self.data)} != {len(other.data)}"
            )

    def _elementwise(self, other, operation):

        self._validate(other)

        result = []

        for a, b in zip(self.data, other.data):
            result.append(operation(a, b))

        return Tensor(result)

    def __add__(self, other):
        return self._elementwise(other, lambda a, b: a + b)

    def __sub__(self, other):
        return self._elementwise(other, lambda a, b: a - b)

    def __mul__(self, other):
        return self._elementwise(other, lambda a, b: a * b)

    def __truediv__(self, other):
        return self._elementwise(other, lambda a, b: a / b)

    def _get_shape(self, data):

      if not isinstance(data, list):
        return ()

      if len(data) == 0:
        return (0,)

      return (len(data),) + self._get_shape(data[0])