from neuroforge.value import Parameter
from neuroforge.optim import SGD

w = Parameter(5)

w.grad = 2

optimizer = SGD(
    [w],
    learning_rate=0.1
)

print("Before:", w)

optimizer.step()

print("After:", w)