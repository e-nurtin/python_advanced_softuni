from project.car.car import Car


class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car = None #! One driver can only drive one car!!
        self.number_of_wins = 0  # This is increased each time a driver wins a race!

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name should contain at least one character!")
        self.__name = value
