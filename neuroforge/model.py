class Sequential:
    
    def __init__(self, layers):
        self.layers = layers
        
    def forward(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x   
    
    
    def parameters(self):

     params = []

     for layer in self.layers:

        if hasattr(layer, "parameters"):
            params.extend(layer.parameters())

     return params 