class Person:
    number_of_isntaces = 0

    def __init__(self, name, age):
        """
        init method is constructor of the object

        :param name: str  instance variable
        :param age: int   instance variable
        """
        self.name = name
        self.age = age
        self.__class__.increment_istances(self.__class__)

    def increment_istances(cls):
        """

        class method
        :return:
        """
        cls.number_of_isntaces += 1

    @staticmethod
    def my_static(call_from):
        print(f'this static method call from {call_from}')

    def __repr__(self):
        return f'person.name = {self.name} person.age= {self.age}'

    def __copy__(self):
        return self.__class__(self.name, self.age)

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


p = Person("david", 29)

print(p)
print(type(p))

p2 = Person("david 2", 39)

print(Person.number_of_isntaces)

p2.my_static(" object")
Person.my_static("Class")
import  copy
p3 = copy.copy(p2)

print(p3 == p2)
print(id(p3) == id(p2))
print(p2 is p3)


c = object.__new__(Person,"new",2)

print(c)
