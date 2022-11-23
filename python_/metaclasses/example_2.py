# import example_1
class MyMeta(type):

    def __new__(cls, name, bases, dct):
        print("meta: creating %s %s" % (name, bases))

        return type.__new__(cls, name, bases, dct)

    def __call__(cls, *args, **kwargs):
        a = super()
        n = super
        return super().__call__(*args, **kwargs)



class Human(metaclass=MyMeta):

    def __call__(self, *args, **kwargs):
        a = super()
        n = super
        return super().__call__(*args, **kwargs)

    def __new__(cls, first_name=None):
        # cls = Human. cls is the class using which the object will be created.
        # Created object will be of type cls.
        # We must call the object class' __new__ to allocate memory
        obj = super().__new__(cls)  # This is equivalent to object.__new__(cls)

        # Modify the object created
        if first_name:
            obj.name = first_name
        else:
            obj.name = "Virat"

        print(type(obj))  # Prints: <__main__.Human object at 0x103665668>
        # return the object
        return obj


virat = Human()

print(virat.name)  # Output: Virat

sachin = Human("Sachin")
print(sachin.name)
