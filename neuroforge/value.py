class Value:
    
    def __init__(self, data, _children=(), _op=''):
        
        self.data = data
        
        self.grad = 0.0
        
        self._prev = set(_children)
        
    def __repr__(self):

       return (
         f"Value("
         f"data={self.data}, "
         f"grad={self.grad}"
         f")"
       )
       
    def __add__(self, other):
        
        if not isinstance(other, Value):
            other = Value(other)
            
        return Value(self.data + other.data,
                     (self, other), '+')    
    
    def __mul__(self, other):
        
        if not isinstance(other, Value):
            other = Value(other)
            
        return Value(self.data * other.data,
                     (self, other), '*')    
