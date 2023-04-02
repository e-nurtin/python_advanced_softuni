from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    INITIAL_SIZE = 5

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, SaltwaterFish.INITIAL_SIZE, price)

    def eat(self):
        self.size += 2

    @property
    def aquarium_type(self):
        return "SaltwaterAquarium"
