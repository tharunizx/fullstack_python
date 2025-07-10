from abc import ABC, abstractmethod
class Application(ABC):
    @abstractmethod
    def turn_on(self):
        pass
class Fridge(Application):
    def turn_on(self):
        print("Fridge turned on")
class WashingMachine(Application):
    def turn_on(self):
        print("WashingMachine turned on")
f=Fridge()
w=WashingMachine()
f.turn_on()
w.turn_on()
