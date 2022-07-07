# example
def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")


greet("DAS")

# docstring
print(greet.__doc__)
#
# example of return
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))

print(absolute_value(-4))


"""
    Built-in functions - Functions that are built into Python.
    User-defined functions - Functions defined by the users themselves.

"""