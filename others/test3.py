class A:
    def __init__(self):
        self.__x = 10
        self._x = 11

    def __wow(self):
        print(f'i am {self.__class__.__name__}')

    def _wow(self):
        print(f'i am {A.__name__}')

    def __wow__(self):
        print(f'i am {self.__class__.__name__}')
    def a_funct(self):
        print("I am a funct")

class B(A):

    def __init__(self):
        super().__init__()

    def get_x(self) -> int:
        #print(self.__x)
        return self._x



    def _wow(self):
        super()._wow()
        print(f'i am {self.__class__.__name__}')

    def __wow__(self):
        print(f'i am {self.__class__.__name__}')

    def execute_a(self):
        self.a_funct()


a = A()
b = B()
b._wow()
b.a_funct()

print(b.get_x())
