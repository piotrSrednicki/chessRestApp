from flask import Flask, jsonify, abort
from flask import make_response

from models.BishopFigure import BishopFigure
from models.Chessboard import Chessboard
from models.KingFigure import KingFigure
from models.KnightFigure import KnightFigure
from models.PawnFigure import PawnFigure
from models.QueenFigure import QueenFigure
from models.RookFigure import RookFigure

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/api/v1/<chess_figure>/<current_field>', methods=['GET'])
def list_available_moves(chess_figure: str, current_field: str):
    chessboard: Chessboard = Chessboard()
    possible_figures_mapping: dict[str] = {
        "bishop": BishopFigure,
        "king": KingFigure,
        'knight': KnightFigure,
        "pawn": PawnFigure,
        "queen": QueenFigure,
        "rook": RookFigure

    }
    output: dict = {}
    correct_figure = False
    for figure in possible_figures_mapping:
        if figure == chess_figure:
            correct_figure = True
            output["availableMoves"] = possible_figures_mapping[figure](
                chessboard.chess_Position_Str_To_Int_Touple(current_field.upper())).list_available_moves()
    output["figure"] = chess_figure
    output["currentField"] = current_field
    if len(output["availableMoves"]) != 0:
        output["error"] = None
    else:
        output["error"] = "Field does not exist"
        return field_error(output)
    if not correct_figure:
        output["error"] = "Figure does not exist"
        return figure_error(output)
    return jsonify(output)


@app.route('/api/v1/<chess_figure>/<current_field>/<dest_field>', methods=['GET'])
def validate_move(chess_figure: str, current_field: str, dest_field: str):
    chessboard: Chessboard = Chessboard()
    possible_figures_mapping: dict[str] = {
        "bishop": BishopFigure,
        "king": KingFigure,
        'knight': KnightFigure,
        "pawn": PawnFigure,
        "queen": QueenFigure,
        "rook": RookFigure

    }
    output: dict = {}
    correct_figure: bool = False
    for figure in possible_figures_mapping:
        if figure == chess_figure:
            correct_figure = True
            output["move"] = possible_figures_mapping[figure](
                chessboard.chess_Position_Str_To_Int_Touple(current_field.upper())).validate_move(
                chessboard.chess_Position_Str_To_Int_Touple(dest_field.upper()))
    output["figure"] = chess_figure
    output["currentField"] = current_field
    output["destField"] = dest_field
    if output["move"] == "valid":
        output["error"] = None
    else:
        output["error"] = "Current move is not permitted"
        return field_error(output)
    if not correct_figure:
        output["error"] = "Figure does not exist"
        return figure_error(output)
    return jsonify(output)


def field_error(message):
    response = jsonify({'message': message})
    response.status_code = 409
    return response

def figure_error(message):
    response = jsonify({'message': message})
    response.status_code = 404
    return response

@app.errorhandler(500)
def server_error(error):
    response = jsonify(error)
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run()
