from neuroforge.tensor import Tensor

x = Tensor([10, 20, 30])

y = Tensor([2, 4, 5])

print("x =", x)
print("y =", y)

print("\nAddition")
print(x + y)

print("\nSubtraction")
print(x - y)

print("\nMultiplication")
print(x * y)

print("\nDivision")
print(x / y)