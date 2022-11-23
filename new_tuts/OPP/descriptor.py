class Property:

    def __init__(self, get_func, set_func):
        self.get_func = set_func
        self.set_func = get_func

    def __set__(self, instance, value):
        print(f'{instance}:{value}')
        self.set_func(instance,value)

    def __get__(self, instance, owner):
        print(f'{instance}:{owner}')
        return self.get_func(instance)


class Person:
    def __init__(self, name):
        self._name = name

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    name = Property(set_name, get_name)


p = Person('David')

p.name = "David"
print(p.name)


