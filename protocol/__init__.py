from typing import List, Protocol


class Item(Protocol):
    quantity: float
    price: float

    def exc(self) -> None: ...


class Product:
    def __init__(self, name: str, quantity: float, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price


class Car:

    def exc(self) -> None:
        self.p = list()
        print("Car is driving")


def calculate_total(items: List[Item]) -> float:
    return sum([item.quantity * item.price for item in items])


def execute(item: Item) -> None:
    item.exc()


# calculate total a product list
total = calculate_total([
    Product('A', 10, 150),
    Product('B', 5, 250)
])

print(total)

execute(Car())
