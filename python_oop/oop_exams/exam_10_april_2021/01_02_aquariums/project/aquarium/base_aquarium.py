from abc import ABC, abstractmethod
from typing import List
from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish
from project.validation.validation import Validation


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: List[BaseDecoration] = []
        self.fish: List[BaseFish] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.empty_string(value, 'Aquarium name')
        self.__name = value

    def calculate_comfort(self):
        return sum(d.comfort for d in self.decorations)

    def add_fish(self, fish: BaseFish):
        if self.capacity == len(self.fish):
            return "Not enough capacity."
        self.fish.append(fish)
        return f"Successfully added {type(fish).__name__} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = [f"{self.name}:"]
        result.append(f"Fish: "
                      f"{' '.join([f.name for f in self.fish]) if self.fish else 'none'}")
        result.append(f"Decorations: {len(self.decorations)}")
        result.append(f"Comfort: {self.calculate_comfort()}")

        return '\n'.join(result)
