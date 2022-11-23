
class Example:
    pass

print(type(Example))


class MyMetaClass(type):
    pass


print(type(MyMetaClass))

print(type(type))

DataCampClass = type('DataCamp', (), {})
print(DataCampClass)
