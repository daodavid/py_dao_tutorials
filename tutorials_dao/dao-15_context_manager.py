import os


# file = open('some_file', 'w')
# try:
#     file.write('Hola!')
# finally:
#     file.close()
#
#
# with open('data.txt') as f:
#     data = f.readlines()
#     print(int(data[0])

class Custom:

    def __init__(self, name):
        self.name = name


    def  __enter__(self):
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"the object {self.name} is being closed...")


    def do_job(self):
        for i in range(0,10):
            os.system('clear')
            print(f"doing job : {self.name}")


myJob = Custom("sql insert")

with myJob as job:
    myJob.do_job()

