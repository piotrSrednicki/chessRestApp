from models.AbstractFigure import Figure

from typing import Tuple


class KnightFigure(Figure):
    def __init__(self, field: Tuple[int, int]):
        super().__init__(field)
        self.moves_list: list[(int, int)] = [
            (-3, 1),
            (-3, -1),
            (3, -1),
            (3, 1),
            (1, 3),
            (1, -3),
            (-1, 3),
            (-1, -3),
        ]