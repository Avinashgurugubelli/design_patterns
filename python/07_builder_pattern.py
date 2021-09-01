"""
What is Builder Design Pattern : Builder Pattern belongs to creational pattern

Definition :
-------------

"Separate the construction of a complex object from its representation so that the same construction process can create different representations"

Builder Pattern solves the situation of increasing constructor parameters and constructors of a given class by providing a step by step initialization of Parameters. After step by step initialisation, it returns the resulting constructed Object at once.


Implementation Guidelines :
---------------------------
We need to Choose Builder Design Pattern when
We need to break up the construction of a complex object
We need to create a complex object and it should be independent of the parts that make up the object
The construction process must allow multiple representations of the same class


The same fluent interface pattern can be now designed as builder pattern.
"""

class PatientInfo:

    def __init__(self) -> None:
        self.name = None
        self.age = None
        self.address = None
        self.phone_number = None
    
    def display(self):
        print("name: {} age: {} phone: {}, address: {}".format(self.name, self.age, self.phone_number, self.address))

class PatientInfobuilder:

    def __init__(self) -> None:
        self.__patientInfo = PatientInfo()

    def set_name(self, name: str):
        self.__patientInfo.name = name
        return self

    def set_age(self, age: int):
        self.__patientInfo.age = age
        return self

    def set_address(self, address: str):
        self.__patientInfo.address = address
        return self

    def set_phone_number(self, phone_number: str):
        self.__patientInfo.phone_number = phone_number
        return self

    def get_instance(self) -> PatientInfo:
        return self.__patientInfo

if __name__ == "__main__":
    p1: PatientInfo = PatientInfobuilder().set_name("Jack").set_age(30).get_instance().display()
    p2: PatientInfo = PatientInfobuilder().set_name("Max").set_address("UK").get_instance().display()


