class ABS:
    def __new__(cls, *args, **kwargs):
        print(f"current class is {cls.__name__}")
        print(f"the parent class is {super().__class__}")
        return super().__new__(cls, *args, **kwargs)

    def execute(self):
        print("execute from ", self.__class__.__name__)


class Button(ABS):
    def __init__(self):
        super().execute()
        self.execute()

    def execute(self):
        print(f"ppp execute {Button}")


abs = ABS()
b = Button()
