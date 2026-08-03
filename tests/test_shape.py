from neuroforge.tensor import Tensor

x = Tensor([1,2,3])

y = Tensor([
    [1,2],
    [3,4]
])

z = Tensor([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])

print(x)
print(y)
print(z)