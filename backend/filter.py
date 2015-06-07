class MyClass:
    
    i = 12345
    
    """A simple example class"""
    def __init__(self):
        print "init"
        
    def f(self):
        
        self.i += 1
        
        return self.i