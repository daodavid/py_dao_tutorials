class SingleltonDad(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingleltonDad, cls).__new__(cls)
        return cls.instance

    def fuck(self):
        print(id(self))


a1 = SingleltonDad()
a2 = SingleltonDad()

a1.fuck()
a2.fuck()


