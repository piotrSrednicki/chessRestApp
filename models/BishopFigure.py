from models.AbstractFigure import Figure

from typing import Tuple


class BishopFigure(Figure):
    def __init__(self, field: Tuple[int, int]):
        super().__init__(field)
        self.moves_list: list[(int, int)] = [
            (x, y)
            for x, y in zip(range(-7, 8), range(-7, 8))
            if x != 0 and y != 0
        ]
        self.moves_list += [
            (x, y)
            for x, y in zip(range(-7, 8), reversed(range(-7, 8)))
            if x != 0 and y != 0
        ]