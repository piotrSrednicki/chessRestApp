from models.AbstractFigure import Figure

from typing import Tuple


class QueenFigure(Figure):
    def __init__(self, field: Tuple[int, int]):
        super().__init__(field)
        self.moves_list: list[(int, int)] = [
            (0, x) for x in range(-7, 8) if x != 0
        ]
        self.moves_list += [
            (x, y)
            for x, y in zip(range(-7, 8), reversed(range(-7, 8)))
            if x != 0 and y != 0
        ]
        self.moves_list += [
            (x, y)
            for x, y in zip(range(-7, 8), range(-7, 8))
            if (x, y) != (0, 0)
        ]
        self.moves_list += [(x, 0) for x in range(-7, 8) if x != 0]