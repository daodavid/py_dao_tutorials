"""
In python there are four types of namespaces scopes:

* built-in namespace
* global
* enclose
* local

These have differing lifetimes. As Python executes a program,
it creates namespaces as necessary and deletes them when they’re no longer needed.
Typically, many namespaces will exist at any given time.
"""

"""
The built-in namespace contains the names of all of Python’s built-in objects.
 These are available at all times when Python is running.
You can list the objects in the built-in namespace with the following command:
"""
import numpy as np
# private
__y = "I am private"
print(dir(__builtins__))
x = 'global scope'


# x = "awesome"

def myfunc():
    print("Python is " + x)
    np.ndarray([1,2,3])


myfunc()


#
def foo():
    x = "enclosing"
    print(x)

    def inner():
        x = "local scope"
        print(x)

        print(x)

    inner()


if __name__ == "__main__" :
    print("DAS")

#
#
foo()

print(x)
