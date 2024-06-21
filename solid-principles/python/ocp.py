
from math import pi

class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2


from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2


#
# class PayementProcessor:
#     def __init__(self, amount):
#         self.amount= amount
#
#     def process_payement(self):
#         pass
#
#
# class Khalti(PayementProcessor):
#
#     def process_payement(self):
#         print("Processing Payement for Khalti",self.amount)
#
# class Esewa(PayementProcessor):
#
#     def process_payement(self):
#         print("Processing Payement for Khalti",self.amount)
#
# class ImePay(PayementProcessor):
#
#     def process_payement(self):
#         print("Processing Payement for Khalti",self.amount)
#
# unProcessedPayement= [ Khalti(2), Esewa(5), ImePay(100) ]
#
# def process_remaining_payements(payements):
#   for payement in payements:
#         print(payement.process_payement())
#
#
