from neuroforge.tensor import Tensor

x = Tensor([10,20,30])

y = Tensor([10,20,30])

z = Tensor([1,2,3])

print("Length")

print(len(x))

print()

print("Indexing")

print(x[0])

print(x[1])

print(x[2])

print()

print("Iteration")

for value in x:
    print(value)

print()

print("Equality")

print(x == y)

print(x == z)

print()

print("Membership")

print(20 in x)

print(99 in x)