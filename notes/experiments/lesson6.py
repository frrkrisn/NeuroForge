# ==========================================
# NeuroForge Journey
# Lesson 06 - Activation Functions
# ==========================================

import  math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    if x > 0:
        return x
    return 0


def tanh(x):
    return math.tanh(x)

number = - 5

print("Sigmoid :", sigmoid(number))
print("ReLU    :", relu(number))
print("Tanh    :", tanh(number))