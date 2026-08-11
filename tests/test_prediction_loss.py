from neuroforge.layers import Linear
from neuroforge.activations import ReLU, Sigmoid
from neuroforge.model import Sequential
from neuroforge.losses import MSELoss

model = Sequential(

    Linear(
        weights=[
            [1,2],
            [3,4]
        ],
        bias=[0,0]
    ),

    ReLU(),

    Linear(
        weights=[
            [1],
            [1]
        ],
        bias=[0]
    ),

    Sigmoid()

)

loss_fn = MSELoss()

x = [[2,3]]

target = [[1]]

prediction = model.forward(x)

loss = loss_fn.forward(
    prediction,
    target
)

print("Prediction:")
print(prediction)

print()

print("Loss:")
print(loss)