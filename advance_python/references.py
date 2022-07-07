
import ctypes
"""So variables are references that point to the objects in the memory.
"""


"""
The id() function returns the memory address of an object referenced by a variable as a base-10 number.

To convert this memory address to a hexadecimal, you use the hex() function:

"""
counter = 10
print(hex(id(counter)))
print(id(counter))


"""
The integer object with the value of 100 has one reference 
which is the counter variable. If you assign the counter to another variable e.g., max:
"""

max = counter

print(hex(id(max)))
print(id(max))



numbers = [1, 2, 3]

numbers_id = id(numbers)

def ref_count(address):
    return ctypes.c_long.from_address(address).value


print("numbers" ,ref_count(numbers_id))