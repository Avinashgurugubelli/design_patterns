"""
The state pattern is a behavioral software design pattern that allows an object to alter its behavior when its internal state changes.

The state pattern can be interpreted as a strategy pattern, which is able to switch a strategy through invocations of methods defined in the pattern's interface.

RealTime Analogy:
----------------
This pattern is a behavioral software pattern that its behavior changes when its internal state changes. 
Let’s say that we will create a calculator and it will perform two mathematical operations, Add and Subtractor. 
So, calculator will be an interface that contains one method, Calculate. This calculation operation will be able to change from Add to Subtractor and vice versa. 
In the State pattern, this change can be performed internally, I mean, client will not change this behavior.
Behavior will change automatically and internally when some conditions are provided.
So, program will continue executing according to the current state. This is a basic example for State pattern. 


RealTime Analogy:
----------------
For example, we have a real time scenario. In a traffic signal, the state of the signal changes all the time. 
The red signal which indicates to stop, the green which indicates to go and so on. In this situation, the state of the signal changes from one state to another.
If we implement this scenario in the traditional approach, then it is very clumsy and a maintenance nightmare. We can resolve these kind of problems using state pattern.


For more Info:
https://medium.com/@osmanakar_65575/design-patterns-state-pattern-vs-strategy-pattern-9d6eb760cc0e
https://www.c-sharpcorner.com/article/the-difference-between-the-two-gof-patterns-strategy-and/
https://en.wikipedia.org/wiki/Strategy_pattern
https://en.wikipedia.org/wiki/State_pattern

"""

from abc import ABC, abstractmethod


class TrafficLight:

    def __init__(self) -> None:
        self.state: ITrafficLight = None

    def change(self):
        self.state.change(self)

    def report_state(self):
        self.state.report_state()


class ITrafficLight(ABC):

    @abstractmethod
    def change(self, traffic_light: TrafficLight):
        pass

    @abstractmethod
    def report_state(self):
        pass


class RedTrafficLight(ITrafficLight):

    def change(self, traffic_light: TrafficLight):
        traffic_light.state = GreenTrafficLight()

    def report_state(self):
        print('Red Light')


class OrangeTrafficLight(ITrafficLight):

    def change(self, traffic_light: TrafficLight):
        traffic_light.state = RedTrafficLight()

    def report_state(self):
        print('Orange Light')


class GreenTrafficLight(ITrafficLight):

    def change(self, traffic_light: TrafficLight):
        traffic_light.state = OrangeTrafficLight()

    def report_state(self):
        print('Green Light')


if __name__ == "__main__":
    traffic_light: TrafficLight = TrafficLight()
    traffic_light.state = RedTrafficLight()
    counter: int = 0
    while(counter <= 10):
        traffic_light.change()
        traffic_light.report_state()
        counter = counter+1
