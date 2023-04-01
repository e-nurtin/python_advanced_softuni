class Validation:

    @staticmethod
    def empty_string(value, name_of_object):
        if value == "":
            raise ValueError(f"{name_of_object} cannot be an empty string.")

    @staticmethod
    def equal_or_below_zero(value, name_of_object):
        if value <= 0:
            raise ValueError(f"{name_of_object} cannot be equal to or below zero.")

