from neuroforge.tensor import Tensor

class MSEloss:
    
    def forward(self, prediction, target):
        
        if not isinstance(prediction, Tensor):
            prediction = Tensor(prediction)
            
        if not isinstance(target, Tensor):
            target = Tensor(target)
        
        diff = prediction - target
        
        squared = diff * diff
        
        return squared.mean()        