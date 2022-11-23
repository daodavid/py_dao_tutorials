class MyMeta(type):

    def __new__(cls, name, bases, dct):
        print("meta: creating %s %s" % (name, bases))

        return type.__new__(cls, name, bases, dct)


    def __call__(self, *args, **kwargs):
        print(*args)


class MyClass(metaclass=MyMeta):

    def __init__(self,x):
       self.x = x

    def test(self):
        pass

    def test2(self):
        print("TEST")

MyClass(3)