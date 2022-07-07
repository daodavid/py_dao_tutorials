c = [i for i in range(100)]


# c = [print(f'i={i}',f'j={j}') for j in range(2) for i in range(100)]


# [print(i) for i in c]


class LinkedList:
    class Node:

        def __init__(self, element):
            self.value = element
            self.__next_element = None

        def set_next(self, next):
            self.__next_element = next

        def next_element(self):
            if self.__next_element is None:
                return None
            return self.__next_element

    def __init__(self):
        self.__pointer = None
        self.__root = None
        self.__len = 0
        super().__init__()

    def __next__(self):
        if self.__root_iter is not None:
            val = self.__root_iter.value
            next = self.__root_iter.next_element()
            if next is not None:
                self.__root_iter = next
            else:
                self.__root_iter = None
            return val
        else:
            raise StopIteration

    def __iter__(self):
        self.__root_iter = self.__root
        return self

    def __add__(self, other):
        pass

    def __len__(self):
        return self.__len

    def append(self, element):
        self.__len +=1
        node = self.Node(element)
        if self.__root is None:
            self.__root = node
            self.__pointer = node
        else:
            self.__pointer.set_next(node)
            self.__pointer = node

    def __eq__(self, other):
        return True

    def __call__(self, *args, **kwargs):
        return False
list = LinkedList()
list.append(0)
list.append(2)
list.append(3)
list.append(4)

for i in list:
    print(i)

print(len(list))

print(list == 1)