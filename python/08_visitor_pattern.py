"""
Visitor Pattern:
----------------
    The visitor design pattern is a way of separating an algorithm from an object structure on which it operates.
    A practical result of this separation is the ability to add new operations to existing object structures without modifying the structures. 
    
            "It is one way to follow the open/closed principle."
    
Real-World Analogy:
------------------
    Imagine a seasoned insurance agent who’s eager to get new customers. He can visit every building in a neighborhood, trying to sell insurance to everyone he meets.
     Depending on the type of organization that occupies the building, he can offer specialized insurance policies:
        - If it’s a residential building, he sells medical insurance.
        - If it’s a bank, he sells theft insurance.
        - If it’s a coffee shop, he sells fire and flood insurance (natural_calamity_insurance).
"""

from abc import ABC, abstractmethod
from typing import List


class IInsuranceVisitor(ABC):

    @abstractmethod
    def provide_medical_insurance(self, medical_insurance):
        pass

    @abstractmethod
    def provide_theft_insurance(self, theft_insurance):
        pass

    @abstractmethod
    def provide_natural_calamity_insurance(self, natural_calamity_insurance):
        pass


class IInsurance(ABC):
    @abstractmethod
    def provide_insurance(self, visitor: IInsuranceVisitor):
        pass


class MedicalInsurance(IInsurance):

    def __init__(self, customer_name: str = None, customer_age: str = None, is_smoker: str = None, existing_deseases: List[str] = []) -> None:
        self.insurance_type: str = 'Medical insurance'
        self.customer_name: str = customer_name
        self.customer_age: str = customer_age
        self.is_smoker: bool = is_smoker
        self.existing_deseases: List[str] = existing_deseases

    def provide_insurance(self, visitor: IInsuranceVisitor):
        return visitor.provide_medical_insurance(self)


class TheftInsurance(IInsurance):

    def __init__(self, bank_name: str = None) -> None:
        self.insurance_type = 'Theft Insurance'
        self.bank_name = bank_name

    def provide_insurance(self, visitor: IInsuranceVisitor):
        return visitor.provide_theft_insurance(self)


class NaturalCalamityInsurance(IInsurance):

    def __init__(self,  customer_name: str = None, property_name: str = None, property_value=None, property_construction_date: str = None) -> None:
        self.insurance_type = 'Natural Calamity Insurance'
        self.customer_name: str = customer_name
        self.property_name: str = property_name
        self.property_value = property_value
        self.property_construction_date: str = property_construction_date

    def provide_insurance(self, visitor: IInsuranceVisitor):
        return visitor.provide_natural_calamity_insurance(self)


class InsuranceVisitor(IInsuranceVisitor):

    """
    Python does not support method over riding, else we can name all the methods with same name with diff args.
    """

    def provide_medical_insurance(self, medical_insurance: MedicalInsurance):
        print(
            f"{medical_insurance.insurance_type} issued for name: {medical_insurance.customer_name}")

    def provide_theft_insurance(self, theft_insurance: TheftInsurance):
        print(
            f"{theft_insurance.insurance_type} issued for bank: {theft_insurance.bank_name}")

    def provide_natural_calamity_insurance(self, natural_calamity_insurance: NaturalCalamityInsurance):
        print(f"{natural_calamity_insurance.insurance_type} issued for property: {natural_calamity_insurance.property_name}")


class Insurance(IInsurance):
    def __init__(self, insurance_list: List[IInsurance] = []) -> None:
        self.insurance_list = insurance_list

    def provide_insurance(self, visitor: IInsuranceVisitor):
        for insurance in self.insurance_list:
            insurance.provide_insurance(visitor)


if __name__ == "__main__":
    m = MedicalInsurance(customer_name="Jack")
    t = TheftInsurance(bank_name="City Bank")
    n = NaturalCalamityInsurance(
        customer_name="Martin", property_name="Coffee shop")

    insurance = Insurance(insurance_list= [m, t, n])

    visitor = InsuranceVisitor()
    insurance.provide_insurance(visitor)
