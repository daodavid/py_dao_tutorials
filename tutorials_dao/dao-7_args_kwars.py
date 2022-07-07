"""



"""


def my_func(*args):
    for i in args:
        print(i)


my_func("SA", 1, 4, True)


def my_func(**kwargs):
    for j in kwargs:
        print(f'{j}={kwargs[j]}')


my_func(fuck=1, p=2)


def all(a, b, *args, **kwargs):
    print(f'a = {a} b = = {b}')
    print(f'args = {args} kwargs =  {kwargs}')


all(3, 4, 1, 2, fuck="Da", p=4)


def spec(a, b):
    print(f'a = {a} b  = {b}')


dict = {"a": 1, "b" : 2}
spec(**dict)