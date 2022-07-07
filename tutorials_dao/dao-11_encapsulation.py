class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # using property decorator
    # a getter function
    @property
    def age(self):
        print("getter method called")
        return self.__age

        # a setter function

    @age.setter
    def age(self, a):
        if (a < 18):
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self.__age = a


p = Person("DAD",232)

print(p.age)
