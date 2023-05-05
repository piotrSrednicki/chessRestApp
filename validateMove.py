from listAvailableMove import list_available_moves
from models import AbstractFigure


def validate_move(figure: AbstractFigure, dest_field: tuple) -> str:
    possible_moves = list_available_moves(figure)
    if (
            figure.chessboard.int_Touple_To_Chess_PositionStr(dest_field)
            in possible_moves
    ):
        return "valid"
    return "invalid"
