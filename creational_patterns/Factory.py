from abc import ABC, abstractmethod

"""
A Factory Pattern or Factory Method Pattern says that just define an interface or abstract class for creating an object but let the subclasses decide which class to instantiate.
 In other words, subclasses are responsible to create the instance of the class.
"""


class Localizer(ABC):

    def __init__(self):
        self.init_localizer()
        super().__init__()

    def localize(self, msg):
        return self.translations.get(msg, msg)

    @abstractmethod
    def init_localizer(self):
        pass


class FrenchLocalizer(Localizer):

    def init_localizer(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle": "ciclo"}


class SpanishLocalizer(Localizer):

    def init_localizer(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle": "ciclo"}


class EnglishLocalizer(Localizer):

    def init_localizer(self):
        pass

    def localize(self, msg):
        return msg



def Factory(language="English"):
    localizers = {

        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }
    return localizers[language]()


if __name__ == "__main__":
    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")

    message = ["car", "bike", "cycle"]

    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))
