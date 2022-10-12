from abc import ABC, abstractmethod


class Thread(ABC):

    def start(self):
        self.__verify()
        self.hookMethod1()
        self._run()
        self._destroy()
        self.hookMethod2()

    @abstractmethod
    def _run(self):
        """
        implement main logic
        :return: None
        """

    @staticmethod
    def _destroy(self):
        """

        On desctoying logic
        :return: None
        """

    def hookMethod1(self):
        pass

    def hookMethod2(self):
        pass

    def __verify(self):
        print("The object is being verrified...")


class MyThread(Thread):

    def _destroy(self):
        print("My object is being destroyed")

    def _run(self):
        for i in range(0, 10):
            print(i)

    def hookMethod1(self):
        print("My hook")



def executeThread(t : Thread):
    t.start()


if __name__=="__main__":
    t1 = MyThread()

    executeThread(t1)

