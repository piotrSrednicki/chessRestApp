from models.AbstractFigure import Figure
from models.Chessboard import Chessboard

from typing import Tuple


class RookFigure(Figure):
    def __init__(self, field: Tuple[int, int]):
        super().__init__(field)
        self.moves_list: list[(int, int)] = [
            (0, x) for x in range(-7, 8) if x != 0
        ]
        self.moves_list += [(x, 0) for x in range(-7, 8) if x != 0]