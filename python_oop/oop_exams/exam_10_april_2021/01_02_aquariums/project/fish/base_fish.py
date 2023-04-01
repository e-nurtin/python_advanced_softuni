from abc import ABC, abstractmethod
from project.validation.validation import Validation


class BaseFish(ABC):
    def __init__(self, name: str, species: str, size: int, price: float):
        self.species = species
        self.size = size
        self.price = price
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.empty_string(value, "Fish name")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        Validation.empty_string(value, "Fish species")
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validation.equal_or_below_zero(value, "Price")
        self.__price = value

    @abstractmethod
    def eat(self):
        ...

    @property
    @abstractmethod
    def aquarium_type(self):
        ...

