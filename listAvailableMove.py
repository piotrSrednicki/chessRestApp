from typing import Tuple

from models import AbstractFigure


def list_available_moves(figure: AbstractFigure) -> list[str]:
    if len(figure.field) != 2:
        return []
    if not (
            figure.field[0] in range(figure.min_x_and_y, figure.max_x_and_y + 1)
            and figure.field[1] in range(figure.min_x_and_y, figure.max_x_and_y + 1)
    ):
        return []
    available_moves: list[str] = []
    for move in figure.moves_list:
        position_after_move: Tuple[int, int] = (
            figure.field[0] + move[0],
            figure.field[1] + move[1],
        )
        if position_after_move[0] in range(
                figure.min_x_and_y, figure.max_x_and_y + 1
        ) and position_after_move[1] in range(
            figure.min_x_and_y, figure.max_x_and_y + 1
        ):
            available_moves.append(
                figure.chessboard.int_Touple_To_Chess_PositionStr(
                    position_after_move
                )
            )
    return available_moves