a = 4
b = a

print(a is b)

print(a == b)

c = 4

print(a is c)

print(f"a:{id(a)}", f"a:{id(c)}")

# mutable

ranks = [1, 2, 3]
rates = [1, 2, 3]

result = ranks is rates
print(result)

ranks.append(1)

print(ranks)


class A:

    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return self.number == other.number



a1 = A(100)

a2 = A(100)

print(a1 == a2)
print(a1 is a2)