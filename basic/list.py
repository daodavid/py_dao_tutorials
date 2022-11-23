l = list()

l.append(1)
print(l.append.__doc__)
l.append(2)
l.append(4)

del l[0]
print(l)

print(l.pop())
print(l)
l.pop(0)
print(l)

l.append(4)
l.remove(4)
print(l.index())
