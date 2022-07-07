from abc import ABC, abstractmethod


class MetaInterface():

    def __new__(cls):
        #
        print(f'__new__MetaInterface called from {cls}')
        # raise BaseException("The interface cannot be instated ")


class IPerson(MetaInterface):
    pass


p = IPerson()

print('Finish')


class MetaInterface(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def transfer(self):
        pass

    pass


class IPerson(MetaInterface):
    pass

class Fuck(type):
    pass


#p = IPerson()

print(type(IPerson))
print(type(Fuck))
print('Finish')