# The following syntax is called a ternary operator
a = 20 if 1 > 0 else 0
print(a)


def my_func(a: int, b: int) -> int:
    """
    :param a: like integer
    :param b: like integer
    :return: The sum of two arguments
    """
    return a+b

print(my_func.__doc__)

