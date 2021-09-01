"""

Requirement:
------------
1. Say we have requirement to make few parameters as manadatory and few as optional, while create a obj.

2. 
Provide an option to choose and build configuration of the system which is allocated to the employees. 
The configuration options that user can choose are RAM, HDD, USB Mouse etc. 
Choose the system configurations based on the computer type that we need to build.
For example, A laptop users can choose touch screen and the desktop users can configure keyboard and mouse.


Defnition:
-----------
Fluent Interface : The idea behind a fluent interface is that one can apply multiple properties to an object by connecting them with dots and 
without having to re-specify the object each time.

Fluent Interface Features : Fluent interface is a method for constructing object oriented APIs, 
where the readability of the source code is close to that of ordinary written prose

Fluent interface is normally implemented by using method cascading (concretely method chaining)

Fluent code is much more readable and allows to vary a product’s internal representation
Fluent Encapsulates code for construction and representation and Provides control over steps of an object construction process


Real time Examples:
C# uses fluent programming extensively in LINQ to build queries using the standard query operators. The implementation is based on extension methods

Searching, Sorting, pagination, grouping with a blend of LINQ are some of the real world usage of fluent interface in combination with builder design pattern.

However, it’s not mandatory to implement fluent interfaces with builder design pattern however, the idea of this session is explore and integrate the fluent interface with builder design pattern.

 """


class PatientInfo:

    def __init__(self, name) -> None:
        self.name = name
        self.age = None
        self.address = None
        self.phone_number = None

    def set_name(self, name: str):
        self.name = name
        return self

    def set_age(self, age: int):
        self.age = age
        return self

    def set_address(self, address: str):
        self.address = address
        return self

    def set_phone_number(self, phone_number: str):
        self.phone_number = phone_number
        return self

    def display(self):
        print("name: {} age: {} phone: {}, address: {}".format(self.name, self.age, self.phone_number, self.address))


if __name__ == "__main__":
    p1=PatientInfo("jack").set_phone_number("77777").set_age(30).display()
    p2 = PatientInfo("jack").set_address("india").display()
