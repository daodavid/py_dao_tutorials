from datetime import datetime
import numpy as np


def time(func ):
    def wrapper(*args, **kwargs):
        now = datetime.now().time()
        c = func(*args, **kwargs)
        print(f'time execution of {func.__name__.upper()} = {datetime.now().time().microsecond - now.microsecond}')
        return c

    return wrapper


@time
def foreach(n : int) -> None:
    for i in range(n):
        i + 10


if __name__ == '__main__':
    foreach(100**2)

    a = np.array([[range(0,1000)]])
    sort = time(np.sort)
    c = sort(a)
    print(c)