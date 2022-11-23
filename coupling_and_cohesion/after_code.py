import string
import random
from dataclasses import dataclass


def generate_vehicle_id(length):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


def generate_vehicle_license(id):
    return f"""{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(
        random.choices(string.ascii_uppercase, k=2))}"""


CATALOG_PRICE = {
    "Tesla Model 3": 60000,
    "Volkswagen ID3": 35000,
    "BMW 5": "45000"
}


@dataclass
class Vehicle:
    brand: str

    def __post_init__(self):
        self.vehicle_id = generate_vehicle_id(12)
        self.vehicle_license_id = generate_vehicle_license(self.vehicle_id)
        self.catalogue_price = CATALOG_PRICE[self.brand]
        self.tax_percentage = 0.05
        if self.brand == "Tesla Model 3" or self.brand == "Volkswagen ID3":
            self.tax_percentage = 0.02

        license_plate = generate_vehicle_license(self.vehicle_id)

    def __repr__(self):
        return f"""
                Registration complete. Vehicle information:
                Brand: {self.brand}
                Id: {self.vehicle_id}
                Payable tax: {self.get_payable_tax()}
               """

    def get_payable_tax(self):
        return self.tax_percentage * self.catalogue_price


class Application:

    def register_vehicle(self, brand: string):
        v = Vehicle("Volkswagen ID3")
        print(v)
        # create a registry instance
        # registry = VehicleRegistry()

        # generate a vehicle id of length 12
        # vehicle_id = registry.generate_vehicle_id(12)

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        # license_plate = registry.generate_vehicle_license(vehicle_id)

        # compute the catalogue price
        # catalogue_price = 0
        # if brand == "Tesla Model 3":
        #     catalogue_price = 60000
        # elif brand == "Volkswagen ID3":
        #     catalogue_price = 35000
        # elif brand == "BMW 5":
        #     catalogue_price = 45000

        # compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%)
        # tax_percentage = 0.05
        # if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
        #     tax_percentage = 0.02

        # compute the payable tax
        # payable_tax = tax_percentage * catalogue_price

        # print out the vehicle registration information


if __name__ == "__main__":
    app = Application()
    app.register_vehicle("Volkswagen ID3")
