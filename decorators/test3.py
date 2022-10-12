
import logging
import numpy as np

logging.basicConfig(filename='example.log',
                    level=logging.INFO)




def log(func):


    def inner(*args):
        logging.info(f'call function {func.__name__,    args}')

        return func(*args)
    return inner




def add(x,y):
    return x+y

z = log(add)



@log
def substraction(x,y):
    return x-y

c = log(np.exp)

substraction(3,6)


c(45)