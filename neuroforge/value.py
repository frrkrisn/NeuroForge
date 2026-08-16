class Value:
    
    def __init__(self, data, _children=(), _op=''):
        
        self.data = data
        
        self.grad = 0.0
        
        self._prev = set(_children)
        
        self._backward = lambda: None
        
    def __repr__(self):

       return (
         f"Value("
         f"data={self.data}, "
         f"grad={self.grad}"
         f")"
       )    
    
    def __mul__(self, other):
        
        if not isinstance(other, Value):
            other = Value(other)
        
        out = Value(self.data * other.data,
                    (self, other), '*') 
        
        def _backward():
            
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
            
        out._backward = _backward
        
        return out     
    
    def backward(self):

      topo = []
      visited = set()

      def build_topo(v):

        if v not in visited:

            visited.add(v)

            for child in v._prev:
                build_topo(child)

            topo.append(v)

      build_topo(self)

      self.grad = 1

      for v in reversed(topo):
         v._backward()
            
    def __add__(self, other):

      if not isinstance(other, Value):
         other = Value(other)

      out = Value(
        self.data + other.data,
        (self, other)
      )

      def _backward():

        self.grad += 1 * out.grad

        other.grad += 1 * out.grad

      out._backward = _backward

      return out       
    
    def __pow__(self, exponent):

     if not isinstance(exponent, (int, float)):
        raise TypeError(
            "Power operation requires an integer or float exponent."
        )

     out = Value(
        self.data ** exponent,
        (self,)
     )

     def _backward():

        self.grad += (
            exponent
            * (self.data ** (exponent - 1))
            * out.grad
        )

     out._backward = _backward

     return out 