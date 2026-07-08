from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Driving a Car")

class Bike(Vehicle):
    def drive(self):
        print("Riding a Bike")

class VehicleFactory:

    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type.lower() == "car":
            return Car()
        elif vehicle_type.lower() == "bike":
            return Bike()
        else:
            return None

vehicle = VehicleFactory.get_vehicle("car")
vehicle.drive()

vehicle = VehicleFactory.get_vehicle("bike")
vehicle.drive()