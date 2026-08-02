import math

def relu(x):
    return max(0,x)


def neuron(inputs, weights, bias):
    wieghted_sum = 0

    for i in range(len(inputs)):
        wieghted_sum += inputs[i] * weights[i]

    wieghted_sum += bias
    return relu(wieghted_sum)

inputs = [5, 90, 7]

layer = [
    ([0.8, 0.5, 0.2], 2),
    ([0.3, 0.7, 0.4], -1),
    ([0.9, 0.2, 0.8], 3),
]

outputs = []

for weights, bias in layer:
    outputs.append(neuron(inputs, weights, bias))

print(outputs)