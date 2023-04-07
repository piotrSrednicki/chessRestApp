from models.AbstractFigure import Figure
from models.Chessboard import Chessboard

from typing import Tuple


class KnightFigure(Figure):
    def __init__(self, field: Tuple[int, int]):
        super().__init__(field)
        self.field = field
        # top-left, top, top-right...
        # x - abcd
        # y - 1234
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
        self.min_x_and_y: int = 0
        self.max_x_and_y: int = 7
        self.chessboard: Chessboard = Chessboard()

    def list_available_moves(self) -> list[str]:
        if not (
            self.field[0] in range(self.min_x_and_y, self.max_x_and_y + 1)
            and self.field[1] in range(self.min_x_and_y, self.max_x_and_y + 1)
        ):
            return []
        available_moves: list[str] = []
        position_after_move: Tuple[int, int] = -1, -1
        for move in self.moves_list:
            position_after_move = (
                self.field[0] + move[0],
                self.field[1] + move[1],
            )
            if position_after_move[0] in range(
                self.min_x_and_y, self.max_x_and_y + 1
            ) and position_after_move[1] in range(
                self.min_x_and_y, self.max_x_and_y + 1
            ):
                available_moves.append(
                    self.chessboard.int_Touple_To_Chess_PositionStr(
                        position_after_move
                    )
                )
        return available_moves

    def validate_move(self, dest_field: tuple) -> str:
        possible_moves = self.list_available_moves()
        print(dest_field, possible_moves)
        if (
            self.chessboard.int_Touple_To_Chess_PositionStr(dest_field)
            in possible_moves
        ):
            return "valid"
        return "invalid"
