from typing import Tuple

from models import AbstractFigure
from models.KnightFigure import KnightFigure
from models.PawnFigure import PawnFigure


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


def list_available_moves_including_other_chess_pieces(figure: AbstractFigure) -> list[str]:
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

    print(figure.__class__)
    print(available_moves)
    if figure.__class__ == KnightFigure:
        unavailable_moves = ['d2', 'e2', 'd7', 'e7']
        if figure.chessboard.int_Touple_To_Chess_PositionStr(figure.field).lower() in ['b1', 'g1', 'b8', 'g8']:
            for move in available_moves:
                if move.lower() in unavailable_moves.copy():
                    available_moves.remove(move)
            print(available_moves)
            return available_moves
    if figure.__class__ == PawnFigure:
        unavailable_moves = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1',
                             'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']
        if figure.chessboard.int_Touple_To_Chess_PositionStr(figure.field).lower() in ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
                            'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']:
            for move in available_moves:
                if move.lower() in unavailable_moves.copy():
                    available_moves.remove(move)
            return available_moves
    return []
