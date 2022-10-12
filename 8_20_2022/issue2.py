class A(object):
    def __call__(self):
        super.__call__()

    def __call__(self, *args, **kwargs):
        #super.__call__(A.__class__,*args, **kwargs)
        return super.__call__(2)




    def __new__(cls, x):
      b = object.__new__(cls)
      b.__init__(x)
      return super()

    def __init__(self, x):
        self.x = x



a = A(2)
B = A()
print(A)

