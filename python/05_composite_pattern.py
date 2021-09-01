"""
    Composite pattern:

    Defnition:
    ----------
    The composite pattern describes a group of objects that are treated the same way as a single instance of the same type of object. 
    The intent of a composite is to "compose/create" objects into tree structures to represent part-whole hierarchies. 
    Implementing the composite pattern lets clients treat individual objects and compositions uniformly.

    A Real Life Example: Group Messaging

    Say, There are six people on my contact list:
     1. Mom, 2. Dad, 
     3. Uncle Bob, 4. Cousin Nick, 5. Aunt Julia,
     6. Amy jackson. 

    The Parents group is composed of 
        -Mom and Dad, 
    whereas the Uncle Bob’s Family group is composed of 
        - Uncle Bob, Cousin Nick, and Aunt Julia.
    
                                    Contacts
                                    --------
                                        |
            -----------------------------------------------------------------
            |                           |                                    |
          Parents                   Uncle Bob’s Family                      Amy jacksom
            |                           |                                     
        -----------                ---------------------------------
        |           |              |              |                 |
        MOM        DAD            Uncle Bob      Cousin Nick        Aunt Julia

In this example, Contacts is represented in a tree structure made of nodes. A node is either a group of people or a single person.

If a node is a group of people, like Parents, then it contains other nodes. If a node is a single person, like Mom, then it’s a leaf node.

For example, I can add another node, CollegeFriends, containing four friends, two of which are grouped into the Roommates node.

"""

from abc import ABC, abstractmethod
from typing import List


class IContact(ABC):
    name: str = None,
    phone_number: str = None

    @abstractmethod
    def send_message(self, message: str):
        pass


class Contact(IContact):
    def __init__(self, name: str, phone_number: str) -> None:
        self.name = name
        self.phone_number = phone_number

    def send_message(self, message: str):
        print(
            f'message sent... details: name: {self.name}, message: {message}, phone_number: {self.phone_number}')

class GroupContact(IContact):

    def __init__(self) -> None:
        self.__contacts: List[IContact] = []
    
    def add_contact(self, contact: IContact):
        self.__contacts.append(contact)
    
    def send_message(self, message: str):
        print("--------------- Sending  group message --------------------")
        for contact in self.__contacts:
            contact.send_message(message=message)


if __name__ == "__main__":
    c1: IContact = Contact("mom", "1256389")
    c2: IContact = Contact("dad", "4532164")

    # Sending message individually
    c1.send_message("HI Mom")
    c2.send_message("HI Dad")

    # Sending Group message
    g1: GroupContact = GroupContact()

    # Adding contacts to groups
    g1.add_contact(c1)
    g1.add_contact(c2)

    g1.send_message("Hello Everyone !")
    



