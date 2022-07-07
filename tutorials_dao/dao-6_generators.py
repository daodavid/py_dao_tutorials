"""
Introduced with PEP 255, generator functions are a special kind of function that return a lazy iterator.
These are objects that you can loop over like a list. However, unlike lists,
lazy iterators do not store their contents in memory.
For an overview of iterators in Python, take a look at Python “for” Loops (Definite Iteration).

"""


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


gen = infinite_sequence()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def ite(num):
    x = num % 100
    yield x

    x = x % 10
    yield x


p = ite(230)

for i in p:
    print(i)
