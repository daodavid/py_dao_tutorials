# list conprehesion

p = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(p)

p = [(x ** 2, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(p)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],]

# . Nested List Comprehensions
transpoce_m = [[row[i] for row in matrix] for i in range(4)]



#del
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[-3:-1]
print(a)
del a[-1]
print(a)


#tuples
t = 12345, 54321, 'hello!'
print(t)


t = (1,2,3)
print(t)

a,*b =t

print(a+b[0])


#set
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)


tel = {'jack': 4098, 'sape': 4139}

for i in tel:
    print(i,tel[i])


k = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])


a,b,v = k.values()

print('da',a,b,v)