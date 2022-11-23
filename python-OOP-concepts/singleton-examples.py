def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            _a = class_(*args, **kwargs)
        return _a

    return getinstance


@singleton
class MyClass(object):
    pass


@singleton
class MyClass2(object):
    pass


a = MyClass()

b = MyClass()

print(a)
print(b)

a = MyClass2()

b = MyClass2()

print(a)
print(b)
