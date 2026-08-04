
from neuroforge.tensor import Tensor

A = Tensor([
    [1,2],
    [3,4]
])

B = Tensor([
    [5,6],
    [7,8]
])

C = A @ B

print(C)