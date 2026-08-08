"""
NeuroForge Layers
"""

from neuroforge.activations import relu
from neuroforge.tensor import Tensor


class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def forward(self, inputs):
        weighted_sum = 0

        for i in range(len(inputs)):
            weighted_sum += inputs[i] * self.weights[i]

        weighted_sum += self.bias

        return relu(weighted_sum)

class Layer:
     def __init__(self, neurons):
        self.neurons = neurons

     def forward(self, inputs):
        outputs = []

        for neuron in self.neurons:
            outputs.append(neuron.forward(inputs))

        return outputs
    
    
class Linear:

    def __init__(self, weights, bias):

        self.weights = Tensor(weights)
        self.bias = Tensor(bias)

    def forward(self, x):

        x = Tensor(x)

        return (x @ self.weights) + self.bias    