from neuroforge.value import Value

a = Value(2)

b = Value(3)

c = a + b

c.backward()

print("c =", c.data)

print("a.grad =", a.grad)

print("b.grad =", b.grad)
