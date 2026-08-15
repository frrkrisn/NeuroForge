from neuroforge.value import Value

a= Value(2)

b = Value(3)

c = Value(4)

d = (a * b) + c

print("d =", d.data)