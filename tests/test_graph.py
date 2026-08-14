from neuroforge.value import Value

a = Value(2)

b = Value(3)

c = a * b

print(c)

print()

print("Parents:")

print(c._prev)