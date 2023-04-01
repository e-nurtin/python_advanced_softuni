from typing import List

from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:
    def __init__(self):
        self.decorations: List[BaseDecoration] = []

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration):
        self.decorations.remove(decoration)

    def find_by_type(self, decoration_type: str):
        for decoration in self.decorations:
            if decoration_type == type(decoration).__name__:
                return decoration
        return "None"
