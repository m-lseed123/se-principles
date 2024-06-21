### Without LSP
from abc import ABC, abstractmethod


class Vehicle:
    def start_engine(self):
        pass

    def accelerate(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def accelerate(self):
        print("Car accelerating")

class Bicycle(Vehicle):
    def start_engine(self):
        raise NotImplementedError("Bicycles don't have engines")

    def accelerate(self):
        print("Bicycle speeding up")

# Usage
def drive(vehicle):
    vehicle.start_engine()
    vehicle.accelerate()

car = Car()
drive(car)

bicycle = Bicycle()
drive(bicycle)



#With LSP



class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def accelerate(self):
        print("Car accelerating")

class Bicycle(Vehicle):
    def accelerate(self):
        print("Bicycle speeding up")

# Usage
def drive(vehicle):
    vehicle.start_engine()  # Now we can safely call start_engine() for all vehicles
    vehicle.accelerate()

car = Car()
drive(car)

bicycle = Bicycle()
drive(bicycle)
