
class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __setattr__(self, key, value):
        print(f'{key} : {value}')
        super.__setattr__(self,key,value)



p1 = Person("David",23)
p1.name = "FFA"

print(p1.name)