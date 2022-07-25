class A:

    def __init__(self):
        self.__x = 0

    @property
    def x(self):
        print("getter method called")
        return self.__x

    @x.setter
    def x(self, a):
        if (a < -1):
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self.__x = a


    def __repr__(self):
        return f"I am {self.__class__.__name__}"


class B(A):
     # def __init__(self):
     #     self._y = 10
     pass


b = B()
a = A()
b.x =4
print(b.x)
print(b.__x)



