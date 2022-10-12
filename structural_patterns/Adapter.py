"""
The adapter pattern is used to chain two different, incompatible interfaces.

"""

def execute(request):
    request.request()


class HTTP():

    def request(self):
        print("HTTP REQUEST",self.__class__)



class HTTPS():



    def securedRequest(self):
        print("secured HTTP REQUEST", self.__class__)



class AddapterReuqst(HTTP, HTTPS):

    def request(self):
        self.securedRequest()

a = AddapterReuqst()

execute()
