from flask import Flask, jsonify

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

    for figure in possible_figures_mapping:
        if figure == chess_figure:
            correct_figure = True
            if chessboard.chess_Position_Str_To_Int_Touple(
                current_field.upper()
            ) == (
                -1,
                -1,
            ):
                wrong_field = True
                output["availableMoves"] = []
            else:
                output["availableMoves"] = possible_figures_mapping[figure](
                    chessboard.chess_Position_Str_To_Int_Touple(
                        current_field.upper()
                    )
                ).list_available_moves()

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
    current_field_tuple: tuple[int, int] = -1, -1
    current_field_tuple = chessboard.chess_Position_Str_To_Int_Touple(
        current_field.upper()
    )
    dest_field_tuple: tuple[int, int] = -1, -1
    dest_field_tuple = chessboard.chess_Position_Str_To_Int_Touple(
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
                output["move"] = possible_figures_mapping[figure](
                    current_field_tuple
                ).validate_move(dest_field_tuple)

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
    response = jsonify({"message": message})
    response.status_code = 409
    return response


def figure_error(message):
    response = jsonify({"message": message})
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run()
