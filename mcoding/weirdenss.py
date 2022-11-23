
#x=4




def exe():
    print(x)


def dec(func):
    x = 5
    def wrppep():
        x =3
        exe(x=4)
    return wrppep


dec(exe)()



