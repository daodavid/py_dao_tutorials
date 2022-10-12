
def logger(func,*args, **kwargs):
    print(func.__name__)
    return func(*args,**kwargs)





def add(x,y):
    return x+y

logger(add,2,4)


#add(2,4)