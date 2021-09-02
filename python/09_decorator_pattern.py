"""
Decorator pattern allows a user to add new functionality to an existing object without altering its structure.
This type of design pattern comes under structural pattern as this pattern acts as a wrapper to existing class.

This pattern creates a decorator class which wraps the original class and provides additional functionality keeping class methods signature intact.

Realtime Analogy:
----------------

Consider a case of a pizza shop.
    - In the pizza shop they will sell few pizza varieties and they will also provide toppings in the menu.
    - Now imagine a situation wherein if the pizza shop has to provide prices for each combination of pizza and topping. 
    Even if there are four basic pizzas and 8 different toppings, the application would go crazy maintaining all these concrete combination of pizzas and toppings.

Here comes the decorator pattern.

As per the decorator pattern, you will implement toppings as decorators and pizzas will be decorated by those toppings' decorators. 
Practically each customer would want toppings of his desire and final bill-amount will be composed of the base pizzas and additionally ordered toppings. 
Each topping decorator would know about the pizzas that it is decorating and it's price. 
GetPrice() method of Topping object would return cumulative price of both pizza and the topping.
"""

from abc import ABC, abstractmethod


class BasePizza(ABC):
    _price: int = None
    _name: str = None

    @abstractmethod
    def get_price(self):
        return self._price


class Margherita(BasePizza):
    def __init__(self) -> None:
        self._price = 100
        self._name = "Margherita"


class Gourmet(BasePizza):
    def __init__(self) -> None:
        self._price = 200
        self._name = "Gourmet"


class ToppingsDecorator(BasePizza):

    def __init__(self, base_pizza: BasePizza) -> None:
        self.base_pizza = base_pizza

    def get_price(self):
        return self._price + self.base_pizza.get_price()


class ExtraCheeseTopping(ToppingsDecorator):
    def __init__(self, base_pizza: BasePizza) -> None:
        self._price = 25
        self._name = "ExtraCheeseTopping"
        super().__init__(base_pizza)


class MushroomTopping(ToppingsDecorator):
    def __init__(self, base_pizza: BasePizza) -> None:
        self._price = 35
        self._name = "MushroomTopping"
        super().__init__(base_pizza)


class JalapenoTopping(ToppingsDecorator):
    def __init__(self, base_pizza: BasePizza) -> None:
        self._price = 55
        self._name = "JalapenoTopping"
        super().__init__(base_pizza)


if __name__ == "__main__":
    margheritaPizza = Margherita()
    print(f"Plain Margherita : {margheritaPizza.get_price()}")

    moreCheese = ExtraCheeseTopping(margheritaPizza)
    someMoreCheese = ExtraCheeseTopping(moreCheese)
    print(
        f"Plain Margherita with double extra cheese: {someMoreCheese.get_price()}")

    moreMushroom = MushroomTopping(someMoreCheese)
    print(f"Plain Margherita with double extra cheese with mushroom:  {moreMushroom.get_price()}")

    moreJalapeno = JalapenoTopping(moreMushroom)
    print(
        f"Plain Margherita with double extra cheese with mushroom with Jalapeno: {moreJalapeno.get_price()}")
