def singleton(cls):
    print(cls)
    cls.__new__ =
    return cls


@singleton
class A:
    def __init__(self):
        msg = f'initializing object of {A}'
        print(msg)


a = A()
