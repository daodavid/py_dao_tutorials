"""
Lists, tuples, dictionaries, and sets are all iterable objects.
They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator:

"""


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


# Strings are also iterable objects, containing a sequence of characters:

name = 'david'

name_iter = iter(name)

print(next(name_iter))
print(next(name_iter))
print(next(name_iter))


"""
for loop works on iterable object
"""