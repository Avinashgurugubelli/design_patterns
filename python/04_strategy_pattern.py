"""
    Strategy design pattern:
    -----------------------

    In computer programming, the strategy pattern (also known as the policy pattern) is a behavioral software design pattern that enables selecting an algorithm at runtime. 
    Instead of implementing a single algorithm directly, code receives run-time instructions as to which in a family of algorithms to use.


    For instance, a class that performs validation on incoming data may use the strategy pattern to select a validation algorithm depending on 
        - the type of data, 
        - the source of the data,
        - user choice, or other discriminating factors.
    These factors are not known until run-time and may require radically different validation to be performed. 
    The validation algorithms (strategies), encapsulated separately from the validating object, may be used by other validating objects in different areas of the system (or even different systems) without code duplication.
    """

from enum import Enum


class SubType(Enum):
    SPINNER = 1,
    SLIDER = 2,
    HOPPER = 3


class IUIElement:

    def __init__(self) -> None:
        self._subtype = None
        self.speed: float = None
        self.glow: float = None
        self.energy: float = None

    def move(self):
        pass


class IUiElementBaseBuilder:
    def __init__(self) -> None:
        self.__ui_element: IUIElement = IUIElement()

    def set_speed(self, speed: float):
        self.__ui_element.speed = speed
        return self

    def set_glow(self, glow: float):
        self.__ui_element.glow = glow
        return self

    def set_energy(self, energy: float):
        self.__ui_element.energy = energy
        return self

    def get_instance(self):
        return self.__ui_element


class SpinnerBuilder(IUiElementBaseBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.spinner: Spinner = Spinner()

    def set_clockwise(self, clockWise: bool):
        self.spinner.clockWise = clockWise
        return self

    def set_expand(self, expand: bool):
        self.spinner.clockWise = expand
        return self

    def get_instance(self):
        return self.spinner


class SliderBuilder(IUiElementBaseBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.slider: Slider = Slider()

    def set_vertical(self, vertical: bool):
        self.slider.vertical = vertical
        return self

    def set_distance(self, distance: int):
        self.slider.distance = distance
        return self

    def get_instance(self):
        return self.slider


class HoperBuilder(IUiElementBaseBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.hopper: Hopper = Hopper()

    def set_visible(self, visible: bool):
        self.hopper.vertical = visible
        return self

    def set_x_cordinate(self, x_cordinate: int):
        self.hopper.x_cordinate = x_cordinate
        return self

    def set_x_cordinate(self, y_cordinate: int):
        self.hopper.y_cordinate = y_cordinate
        return self

    def get_instance(self):
        return self.hopper


class Spinner(IUIElement):
    def __init__(self) -> None:
        self._subtype = SubType.SPINNER
        self.clockWise: bool = None
        self.expand: bool = None

    def move(self):
        return 'Spinner moved'


class Slider(IUIElement):
    def __init__(self) -> None:
        self._subtype = SubType.SLIDER
        self.vertical: bool = None
        self.distance: int = None

    def move(self):
        return 'Slider moved'


class Hopper(IUIElement):
    def __init__(self) -> None:
        self._subtype = SubType.HOPPER
        self.visible: bool = None
        self.x_cordinate: int = None
        self.y_cordinate: int = None

    def move(self):
        return 'Hopper moved'


class Icon():

    def __init__(self, ui_element: IUIElement) -> None:
        self.ui_element = ui_element

    """
    Here in run time, dynamically evaluate the move function, based on the element type. 
    """
    def move(self):
        attrs = ' '.join("'%s': '%s'" % item for item in vars(
            self.ui_element).items())
        print(f'{self.ui_element.move()} with attributes, {attrs}')


if __name__ == "__main__":
    # Builder pattern
    hopper = HoperBuilder().set_energy(1).set_glow(True).set_x_cordinate(1).get_instance()
    # Builder pattern
    spinner = SpinnerBuilder().set_expand(True).set_clockwise(True).get_instance()
    # Builder pattern
    slider = SliderBuilder().set_distance(2).set_vertical(True).get_instance()

    Icon(hopper).move()
    Icon(spinner).move()
