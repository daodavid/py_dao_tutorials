from io import StringIO

file = StringIO("DS")

# this will read the file
print(file.read())

# We can also write this file.
file.write(" Welcome to geeksforgeeks.")

# This will make the cursor at
# index 0.
file.seek(0)

# This will print the file after
# writing in the initial string.
print('The string after writing is:', file.read())


class DecoratorWriter(StringIO):

    def __init__(self, writter : StringIO):
        self.writer = writter

    def write(self, s: str):
        self.writer(s)


class DecodeStringIO(DecoratorWriter):

    @staticmethod
    def _encode(s :str) -> str:
        return str(str.encode( "utf-8")) +str(11)

    def write(self, s : str):
        self.writer.write(str(DecodeStringIO._encode(s)))

    def read(self):
        return self.writer.read()

    def seek(self, offset: int, whence: int = ...):


file = DecodeStringIO(StringIO("David"))

file.write(" Welcome to geeksforgeeks.")


file.writer.write("DASDAS")
file.writer.seek(0)
print('The string using decode:', file.writer.read())

file.writer.seek(0)

print('The string using decode:', file.read())
