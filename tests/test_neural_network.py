from neuroforge.layers import Linear
from neuroforge.activations import ReLU, Sigmoid
from neuroforge.model import Sequential

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

x = [[2,3]]

prediction = model.forward(x)

print(prediction)