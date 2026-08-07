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

    def __iter__(self):
        return iter(self.data)

    def __eq__(self, other):
        if not isinstance(other, Tensor):
            return False
        return self.data == other.data

    def __repr__(self):
        return f"Tensor(data={self.data}, shape={self.shape})"

    # -----------------------------
    # Validation
    # -----------------------------

    def _validate(self, other):
        if len(self.data) != len(other.data):
            raise ValueError(
                f"Tensor size mismatch: {len(self.data)} != {len(other.data)}"
            )

    # -----------------------------
    # Elementwise Operations
    # -----------------------------

    def _elementwise(self, other, operation):

        # Tensor vs Tensor
        if isinstance(other, Tensor):

            self._validate(other)

            result = []

            for a, b in zip(self.data, other.data):
                result.append(operation(a, b))

            return Tensor(result)

        # Tensor vs Scalar
        elif isinstance(other, (int, float)):

            result = []

            for value in self.data:
                result.append(operation(value, other))

            return Tensor(result)

        else:
            raise TypeError(
                f"Unsupported operand type: {type(other)}"
            )

    # -----------------------------
    # Arithmetic
    # -----------------------------

    def __add__(self, other):
        return self._elementwise(other, lambda a, b: a + b)

    def __sub__(self, other):
        return self._elementwise(other, lambda a, b: a - b)

    def __mul__(self, other):
        return self._elementwise(other, lambda a, b: a * b)

    def __truediv__(self, other):
        return self._elementwise(other, lambda a, b: a / b)


    def __matmul__(self, other):

      if not isinstance(other, Tensor):
        raise TypeError("Matrix multiplication requires another Tensor.")
 
      if len(self.shape) != 2 or len(other.shape) != 2:
        raise ValueError("Matrix multiplication requires 2D tensors.")

      rows_a, cols_a = self.shape
      rows_b, cols_b = other.shape

      if cols_a != rows_b:
        raise ValueError(
            f"Cannot multiply shapes {self.shape} and {other.shape}"
        )

      result = []

      for i in range(rows_a):

        row = []

        for j in range(cols_b):

            value = 0

            for k in range(cols_a):

                value += self.data[i][k] * other.data[k][j]

            row.append(value)

      result.append(row)


      return Tensor(result)    
    

    def transpose(self):

     if len(self.shape) != 2:
        raise ValueError(
            "Transpose is only supported for 2D tensors."
        )

     rows, cols = self.shape

     result = []

     for j in range(cols):

        new_row = []

        for i in range(rows):

            new_row.append(self.data[i][j])

        result.append(new_row)

     return Tensor(result)

    @property
    def T(self):
        return self.transpose()

    # -----------------------------
    # Reverse Arithmetic
    # -----------------------------

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):

        result = []

        for value in self.data:
            result.append(other - value)

        return Tensor(result)

    def __rmul__(self, other):
        return self.__mul__(other)


    def sum(self):

     flat = self._flatten(self.data)

     total = 0

     for value in flat:
        total += value

     return total
 
 
    def mean(self):

     flat = self._flatten(self.data)

     return sum(flat) / len(flat)
    # -----------------------------
    # Shape
    # -----------------------------

    def _get_shape(self, data):

        if not isinstance(data, list):
            return ()

        if len(data) == 0:
            return (0,)

        return (len(data),) + self._get_shape(data[0])

    # -----------------------------
    # Structure Validation
    # -----------------------------

    def _validate_structure(self, data):

        if not isinstance(data, list):
            return

        if len(data) == 0:
            return

        first_is_list = isinstance(data[0], list)

        for item in data:

            if isinstance(item, list) != first_is_list:
                raise ValueError(
                    "Invalid Tensor: mixed list and scalar elements."
                )

        if first_is_list:

            expected_length = len(data[0])

            for row in data:

                if len(row) != expected_length:
                    raise ValueError(
                        "Invalid Tensor: jagged arrays are not allowed."
                    )

                self._validate_structure(row)


    def _flatten(self, data):

      if not isinstance(data, list):
        return [data]

      result = []

      for item in data:
        result.extend(self._flatten(item))

      return result  

    def _build_shape(self, flat, rows, cols):

     result = []

     index = 0

     for i in range(rows):

        row = []

        for j in range(cols):

            row.append(flat[index])

            index += 1

        result.append(row)

        return result           