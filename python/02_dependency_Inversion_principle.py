
"""
In object-oriented design, the dependency inversion principle is a specific form of loosely coupling software modules. When following this principle, the conventional dependency relationships established from high-level, policy-setting modules to low-level, dependency modules are reversed, thus rendering high-level modules independent of the low-level module implementation details. The principle states:[1]

High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g., interfaces).
Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions.

The below program is also an example of strategy pattern:

In computer programming, the strategy pattern (also known as the policy pattern) is a behavioral software design pattern that enables selecting an algorithm (object) at runtime. 
Instead of implementing a single algorithm directly, code receives run-time instructions as to which in a family of algorithms to use.

Here in runtime we are resolving -> to use tester or bulb

"""

from abc import ABC, abstractmethod

class IDevice(ABC):
    
    @abstractmethod
    def glow(self):
        pass

    @abstractmethod
    def dim(self):
        pass

class ICircuit(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def holder(self, device: IDevice):
        pass

class tester(IDevice):
    
    def __init__(self) -> None:
        super().__init__()
        self.__device = "Tester"
    
    def glow(self):
       return "Device: "+ self.__device+ " Glowed"
    
    def dim(self):
       return "Device: "+ self.__device+ " Dimmed"

class Bulb(IDevice):
    
    def __init__(self) -> None:
        super().__init__()
        self.__device = "Bulb"
    
    def glow(self):
       return "Device: "+ self.__device+ " Glowed"
    
    def dim(self):
       return "Device: "+ self.__device+ " Dimmed"

class Circut(ICircuit):
    def holder(self, device: IDevice):
        print(device.glow())
    
    def open(self):
        print("circuit open called")
    
    def close(self):
        print("circuit close called")

if __name__ == "__main__":
    tester = tester()
    bulb = Bulb()
    circuit = Circut()
    circuit.holder(tester)
    circuit.holder(bulb)

        

