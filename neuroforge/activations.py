"""
NeuroForge Activation Functions
Author: Krishna Agrawal
"""

from neuroforge.tensor import Tensor


def relu(x):
    return max(0, x)


class ReLU:

    def forward(self, x):

        if isinstance(x, Tensor):

            def apply(data):

                if isinstance(data, list):
                    return [apply(item) for item in data]

                return max(0, data)

            return Tensor(apply(x.data))

        return max(0, x)

import math

class Sigmoid:

    def forward(self, x):

        if isinstance(x, Tensor):

            def apply(data):

                if isinstance(data, list):
                    return [apply(item) for item in data]

                return 1 / (1 + math.exp(-data))

            return Tensor(apply(x.data))

        return 1 / (1 + math.exp(-x))