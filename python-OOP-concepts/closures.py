class A(int):

    def __init__(self, x):
        self.x = x

    def increment(self):
        self.x = self.x+1

    def is_equal(self,num):
        return self.x ==num


def outer():
    outer1 = A(1)
    def inner():
        if outer1.is_equal(1):
            outer1 = 2
            print('attempted to accessed outer %d' % outer1)

    return inner

