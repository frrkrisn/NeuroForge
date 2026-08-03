"""
NeuroForge Tensor

Author: Krishna Agrawal
"""


class Tensor:

    def __init__(self, data):

        self._validate_structure(data)

        self.data = data

        self.shape = self._get_shape(data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __eq__(self, other):

      if not isinstance(other, Tensor):
        return False

      return self.data == other.data 

    def __iter__(self):
        return iter(self.data)   

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

    def _validate_structure(self, data):
        if not isinstance(data, list):
            return

        if len(data) == 0:
            return

        first_is_list = isinstance(data[0], list)

        for item in data:

            if isinstance(item, list) != first_is_list:
                raise ValueError("Inconsistent structure in tensor data.")

        if first_is_list:

              expected_length = len(data[0])

              for row in data:

                  if len(row) != expected_length:
                        raise ValueError("Inconsistent structure in tensor data.")


                  self._validate_structure(row)
        