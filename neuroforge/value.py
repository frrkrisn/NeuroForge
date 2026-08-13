class Value:
    
    def __init__(self, data):
        
        self.data = data
        
        self.grad = 0.0
        
    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"
       
    def __add__(self, other):
        
        if not isinstance(other, Value):
            other = Value(other)
            
        return Value(self.data + other.data)    
    
    def __mul__(self, other):
        
        if not isinstance(other, Value):
            other = Value(other)
            
        return Value(self.data * other.data)
    