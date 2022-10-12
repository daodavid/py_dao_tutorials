# originated


class Singleton(object):
    __instance = None
    _instance2 = 5

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)

        return cls.__instance

    def __eq__(self, other):
        return True


a = Singleton()

b = Singleton()

print(a)
print(b)
print(a is b)
print(a == b)
