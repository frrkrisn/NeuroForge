from neuroforge.layers import TrainableLinear
from neuroforge.value import Value
from neuroforge.optim import SGD

model = TrainableLinear(
    weight=0,
    bias=0
)

optimizer = SGD(
    model.parameters(),
    learning_rate=0.01
)

x = Value(2)
target = Value(10)

for step in range(20):

    optimizer.zero_grad()

    prediction = model.forward(x)

    error = prediction - target

    loss = error ** 2

    loss.backward()

    optimizer.step()

    print(
        f"Step {step + 1}: "
        f"prediction={prediction.data:.4f}, "
        f"loss={loss.data:.4f}, "
        f"weight={model.weight.data:.4f}, "
        f"bias={model.bias.data:.4f}"
    )