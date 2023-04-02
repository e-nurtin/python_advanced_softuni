from typing import List

from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:
    def __init__(self):
        self.decorations: List[BaseDecoration] = []

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration):
        for decor in self.decorations:
            if decor == decoration:
                self.decorations.remove(decoration)
                return True
        return False

    def find_by_type(self, decoration_type: str):
        for decoration in self.decorations:
            if decoration_type == type(decoration).__name__:
                return decoration
        return "None"
