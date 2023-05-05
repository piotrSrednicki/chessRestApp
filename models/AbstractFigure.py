from abc import ABC
from typing import Tuple

from models.Chessboard import Chessboard


class Figure(ABC):
    def __init__(self, field: Tuple[int, int]):
        self.field = field
        self.min_x_and_y: int = 0
        self.max_x_and_y: int = 7
        self.chessboard: Chessboard = Chessboard()
