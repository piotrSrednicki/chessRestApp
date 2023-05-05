from listAvailableMove import list_available_moves, list_available_moves_including_other_chess_pieces
from models import AbstractFigure


def validate_move(figure: AbstractFigure, dest_field: tuple) -> str:
    possible_moves = list_available_moves(figure)
    if (
            figure.chessboard.int_Touple_To_Chess_PositionStr(dest_field)
            in possible_moves
    ):
        return "valid"
    return "invalid"


def validate_move_including_other_chess_pieces(figure: AbstractFigure, dest_field: tuple) -> str:
    possible_moves = list_available_moves_including_other_chess_pieces(figure)
    if (
            figure.chessboard.int_Touple_To_Chess_PositionStr(dest_field)
            in possible_moves
    ):
        return "valid"
    return "invalid"
