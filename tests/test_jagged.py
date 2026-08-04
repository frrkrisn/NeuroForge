from neuroforge.tensor import Tensor

print("Valid Tensor")

x = Tensor([
    [1,2],
    [3,4]
])

print(x)

print()

print("Invalid Tensor")

y = Tensor([
    [1,2],
    [3]
])

print(y)