from neuroforge.layers import Layer, Neuron

layer = Layer([
    Neuron([0.8, 0.5, 0.2], 2),
    Neuron([0.3, 0.7, 0.4], -1),
    Neuron([0.9, 0.2, 0.8], 3),
])

inputs = [5, 90, 7]

print(layer.forward(inputs))