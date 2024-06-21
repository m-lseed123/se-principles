# Wihout Dependency Inversion, here switch directly depends on LightBulb class  making high class and low class module tightly coupled

class LightBulb:
    def turn_on(self):
        print("LightBulb: Bulb turned on")

    def turn_off(self):
        print("LightBulb: Bulb turned off")

class Switch:
    def __init__(self, bulb):
        self.bulb = bulb

    def toggle(self):
        if self.bulb.turn_on():
            self.bulb.turn_off()
        else:
            self.bulb.turn_on()

bulb = LightBulb()
switch = Switch(bulb) 
switch.toggle()



# With Dependency Inversion, switch class now depends on Switchable abstraction, 
# allowing it to work with any class that implements Switchable , eliminating the tight coupling between Lightbulb and switch
# the low level module becomes easily replacable with any classes =implementing Lightbulb

class Switchable():
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: Bulb turned on")

    def turn_off(self):
        print("LightBulb: Bulb turned off")

class Switch:
    def __init__(self, device):
        self.device = device

    def toggle(self):
        if isinstance(self.device, Switchable):
            self.device.turn_on()
            self.device.turn_off()

bulb = LightBulb()
switch = Switch(bulb)
switch.toggle()


# Without using Inversion of Control 
class Logger:
    def log(self, message):
        with open('log.txt', 'a') as f:
            f.write(message + '\n')

class Calculator:

    def __init__(self):
        self.logger = Logger()

    def add(self, x, y):
        result = x + y
        self.logger.log(f"Added {x} and {y}, result = {result}")
        return result



#using Inversion of control

from abc import ABC, abstractmethod

class LoggerInterface(ABC):
    @abstractmethod
    def log(self, message):
        pass

class Logger(LoggerInterface):
    def log(self, message):
        with open('log.txt', 'a') as f:
            f.write(message + '\n')

class Calculator:
    def __init__(self, logger: LoggerInterface):
        self.logger = logger

    def add(self, x, y):
        result = x + y
        self.logger.log(f"Added {x} and {y}, result = {result}")
        return result
