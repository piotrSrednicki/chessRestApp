from models.AbstractFigure import Figure

from typing import Tuple


class PawnFigure(Figure):
    def __init__(self, field: Tuple[int, int]):
        super().__init__(field)
        self.moves_list: list[(int, int)] = [(0, 1), (0, -1)]
