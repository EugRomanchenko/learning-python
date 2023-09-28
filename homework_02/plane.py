"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, add_cargo):
        if self.cargo + add_cargo <= self.max_cargo:
            self.cargo = self.cargo + add_cargo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo
