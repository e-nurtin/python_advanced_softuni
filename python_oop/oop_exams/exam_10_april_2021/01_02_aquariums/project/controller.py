from typing import List
from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: List[BaseAquarium] = []

    @property
    def aquarium_types(self):
        return {"FreshwaterAquarium": FreshwaterAquarium,
                "SaltwaterAquarium": SaltwaterAquarium}

    @property
    def decoration_types(self):
        return {"Ornament": Ornament, "Plant": Plant}

    @property
    def fish_types(self):
        return {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}

    @staticmethod
    def find_entity_from_name(entities, entity_name):
        for entity in entities:
            if entity.name == entity_name:
                return entity

    @staticmethod
    def __calculate(aquarium):
        return sum(d.price for d in aquarium.decorations) + \
               sum(f.price for f in aquarium.fish)

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.aquarium_types:
            return "Invalid aquarium type."

        aquarium = self.aquarium_types[aquarium_type](aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.decoration_types:
            return "Invalid decoration type."

        decoration = self.decoration_types[decoration_type]()
        self.decorations_repository.add(decoration)

        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.find_entity_from_name(self.aquariums, aquarium_name)
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if decoration != "None" and aquarium:
            self.decorations_repository.remove(decoration)
            aquarium.add_decoration(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."
        return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str,
                 fish_name: str, fish_species: str, price: float):
        if fish_type not in self.fish_types:
            return f"There isn't a fish of type {fish_type}."

        fish = self.fish_types[fish_type](fish_name, fish_species, price)
        aquarium = self.find_entity_from_name(self.aquariums, aquarium_name)

        if fish.aquarium_type != type(aquarium).__name__:
            return "Water not suitable."
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.find_entity_from_name(self.aquariums, aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.find_entity_from_name(self.aquariums, aquarium_name)
        if aquarium:
            return f"The value of Aquarium {aquarium_name} is {self.__calculate(aquarium)}."

    def report(self):
        result = []
        for aquarium in self.aquariums:
            result.append(str(aquarium))

        return '\n'.join(result)
