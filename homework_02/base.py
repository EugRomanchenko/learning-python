from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    def __init__(self, weight: int = 300, fuel: int = 0, fuel_consumption: int = 40):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel > 0:
            self.started = True
        else:
            raise exceptions.LowFuelError

    def move(self, distance):
        if self.fuel // self.fuel_consumption >= distance:
            self.fuel = self.fuel - distance * self.fuel_consumption
        else:
            raise exceptions.NotEnoughFuel

