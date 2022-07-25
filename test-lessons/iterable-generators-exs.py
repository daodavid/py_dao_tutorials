a = range(1, 5)

print(type(a))
print(a.start)

demo = iter(a)

while True:
    try:
        print(next(demo))
    except StopIteration:
        break;


def my_range(start, stop):
    yield start
    while start < stop:
        start = start+1
        yield start




print("custom iteration")
demo = my_range(0,10)
while True:
    try:
        print(next(demo))
    except StopIteration:
        break;

demo = my_range(0,3)
print("loop")
for i in iter(demo) :
    print(i)

print("loop2")
for i in a :
    print(i)

print("loop4")
for i in a :
    print(i)