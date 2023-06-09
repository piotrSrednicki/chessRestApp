from flask import Flask, jsonify

import listAvailableMove
import validateMove
from models.BishopFigure import BishopFigure
from models.Chessboard import Chessboard
from models.KingFigure import KingFigure
from models.KnightFigure import KnightFigure
from models.PawnFigure import PawnFigure
from models.QueenFigure import QueenFigure
from models.RookFigure import RookFigure

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


@app.route("/")
def default_page():
    return "Welcome to chess API"


@app.route("/api/v1/<chess_figure>/<current_field>", methods=["GET"])
def list_available_moves(chess_figure: str, current_field: str):
    chessboard: Chessboard = Chessboard()
    possible_figures_mapping: dict[str] = {
        "bishop": BishopFigure,
        "king": KingFigure,
        "knight": KnightFigure,
        "pawn": PawnFigure,
        "queen": QueenFigure,
        "rook": RookFigure,
    }
    output: dict = {}
    correct_figure: bool = False
    wrong_field: bool = False
    output["availableMoves"] = []
    current_field_tuple: tuple[int, int] = chessboard.chess_Position_Str_To_Int_Touple(
        current_field.upper()
    )

    for figure in possible_figures_mapping:
        if figure == chess_figure:
            correct_figure = True
            if current_field_tuple == (
                    -1,
                    -1,
            ):
                wrong_field = True
                output["availableMoves"] = []
            else:
                output["availableMoves"] = listAvailableMove.list_available_moves(possible_figures_mapping[figure](
                    current_field_tuple))

    output["figure"] = chess_figure
    output["currentField"] = current_field
    output["error"] = None

    if not correct_figure:
        output["error"] = "Figure does not exist"
        return figure_error(output)
    if wrong_field:
        output["error"] = "Field does not exist"
        return field_error(output)
    return jsonify(output)


@app.route(
    "/api/v1/<chess_figure>/<current_field>/<dest_field>", methods=["GET"]
)
def validate_move(chess_figure: str, current_field: str, dest_field: str):
    chessboard: Chessboard = Chessboard()
    possible_figures_mapping: dict[str] = {
        "bishop": BishopFigure,
        "king": KingFigure,
        "knight": KnightFigure,
        "pawn": PawnFigure,
        "queen": QueenFigure,
        "rook": RookFigure,
    }
    output: dict = {}
    correct_figure: bool = False
    wrong_field: bool = False
    output["move"] = "invalid"
    current_field_tuple: tuple[int, int] = chessboard.chess_Position_Str_To_Int_Touple(
        current_field.upper()
    )
    dest_field_tuple: tuple[int, int] = chessboard.chess_Position_Str_To_Int_Touple(
        dest_field.upper()
    )
    for figure in possible_figures_mapping:
        if figure == chess_figure:
            correct_figure = True
            if current_field_tuple == (-1, -1):
                wrong_field = True
                output["move"] = ["invalid"]
            elif dest_field_tuple == (-1, -1):
                wrong_field = True
                output["move"] = ["invalid"]
            else:
                output["move"] = validateMove.validate_move(possible_figures_mapping[figure](
                    current_field_tuple), dest_field_tuple)

    output["figure"] = chess_figure
    output["currentField"] = current_field
    output["destField"] = dest_field
    output["error"] = None

    if not correct_figure:
        output["error"] = "Figure does not exist"
        return figure_error(output)
    if output["move"] == "invalid":
        output["error"] = "Current move is not permitted"
    if wrong_field:
        output["error"] = "Field does not exist"
        return field_error(output)
    return jsonify(output)


@app.route("/api/v1/includeOtherChessPieces/<chess_figure>/<current_field>", methods=["GET"])
def list_available_moves_including_other_chess_pieces(chess_figure: str, current_field: str):
    """
        Trzeba stworzyć obiekty pionków
        Walidacja czy dany pionek jest na odpowiednim miejscu startowym
        Wystarczy dodać sprawdzenie czy na liście dostępnych pól znajdują się pozostałe pionki (UWAGA!
        jeśli pionek znajduje się na polu h1 a kolejny na h2 to nie można ruszyć się na h3!
        [dla niektórych pionków] - blokowanie całej linii)

    """
    chessboard: Chessboard = Chessboard()
    possible_figures_mapping: dict[str] = {
        "bishop": BishopFigure,
        "king": KingFigure,
        "knight": KnightFigure,
        "pawn": PawnFigure,
        "queen": QueenFigure,
        "rook": RookFigure,
    }
    output: dict = {}
    correct_figure: bool = False
    wrong_field: bool = False
    output["availableMoves"] = []
    current_field_tuple: tuple[int, int] = chessboard.chess_Position_Str_To_Int_Touple(
        current_field.upper()
    )

    for figure in possible_figures_mapping:
        if figure == chess_figure:
            correct_figure = True
            if current_field_tuple == (
                    -1,
                    -1,
            ):
                wrong_field = True
                output["availableMoves"] = []
            else:
                output["availableMoves"] = listAvailableMove.list_available_moves_including_other_chess_pieces(possible_figures_mapping[figure](
                    current_field_tuple))

    output["figure"] = chess_figure
    output["currentField"] = current_field
    output["error"] = None

    if not correct_figure:
        output["error"] = "Figure does not exist"
        return figure_error(output)
    if wrong_field:
        output["error"] = "Field does not exist"
        return field_error(output)
    return jsonify(output)


@app.route(
    "/api/v1/includeOtherChessPieces/<chess_figure>/<current_field>/<dest_field>", methods=["GET"]
)
def validate_move_including_other_chess_pieces(chess_figure: str, current_field: str, dest_field: str):
    chessboard: Chessboard = Chessboard()
    possible_figures_mapping: dict[str] = {
        "bishop": BishopFigure,
        "king": KingFigure,
        "knight": KnightFigure,
        "pawn": PawnFigure,
        "queen": QueenFigure,
        "rook": RookFigure,
    }
    output: dict = {}
    correct_figure: bool = False
    wrong_field: bool = False
    output["move"] = "invalid"
    current_field_tuple: tuple[int, int] = chessboard.chess_Position_Str_To_Int_Touple(
        current_field.upper()
    )
    dest_field_tuple: tuple[int, int] = chessboard.chess_Position_Str_To_Int_Touple(
        dest_field.upper()
    )
    for figure in possible_figures_mapping:
        if figure == chess_figure:
            correct_figure = True
            if current_field_tuple == (-1, -1):
                wrong_field = True
                output["move"] = ["invalid"]
            elif dest_field_tuple == (-1, -1):
                wrong_field = True
                output["move"] = ["invalid"]
            else:
                output["move"] = validateMove.validate_move_including_other_chess_pieces(possible_figures_mapping[figure](
                    current_field_tuple), dest_field_tuple)

    output["figure"] = chess_figure
    output["currentField"] = current_field
    output["destField"] = dest_field
    output["error"] = None

    if not correct_figure:
        output["error"] = "Figure does not exist"
        return figure_error(output)
    if output["move"] == "invalid":
        output["error"] = "Current move is not permitted"
    if wrong_field:
        output["error"] = "Field does not exist"
        return field_error(output)
    return jsonify(output)


def field_error(message):
    print(message)
    response = jsonify({"message": message})
    response.status_code = 409
    return response


def figure_error(message):
    print(message)
    response = jsonify({"message": message})
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run()
