from dataclasses import dataclass


@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

    def __setattr__(self, name, value):
        if name == 'age':
            assert value > 0, f"value of {name} can't be negative: {value}"
        self.__dict__[name] = value


a = InventoryItem("DA", '232')
print(a)
print(dir(a))

b = InventoryItem("DA", '232')
print(a)
print(dir(a))
a.name = "DSa"
print(a == b)

print(a is b)
asd