#from test2 import logger
import test2; as r


@r.logger
def add(x,y):
    return x+y



add(2,3)

print("finish")