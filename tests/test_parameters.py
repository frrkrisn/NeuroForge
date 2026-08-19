from neuroforge.model import Sequential
from neuroforge.layers import Linear
from neuroforge.activations import ReLU

model = Sequential(

    Linear(
        weights=[
            [1, 2],
            [3, 4]
        ],
        bias=[0, 0]
    ),

    ReLU(),

    Linear(
        weights=[
            [5],
            [6]
        ],
        bias=[0]
    )
)

params = model.parameters()

print("Number of parameter objects:", len(params))

for i, param in enumerate(params):

    print(
        f"Parameter {i}:",
        param
    )