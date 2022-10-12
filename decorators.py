"""
In order to understand about decorators,
we must first know a few basic things in Python.

We must be comfortable with the fact
that everything in Python (Yes! Even classes), are objects.
Names that we define are simply identifiers bound to these objects.
 Functions are no exceptions, they are objects too (with attributes).
Various different names can be bound to the same function object.

"""

# example
import numpy as np


def first(msg):
    print(msg)


second = first

second("Hello")


# decorator


def ordinary():
    print('I am ordinary func')


def dec(func):
    def inner():
        print("decorated", func)
        func()

    return inner


def derivate(func, x):
    def inner(x, h=0.001):
        return (func(x + h) - func(x)) / h

    return inner


a = derivate(np.exp, 2)

print(a(3))
print(np.exp(3))




