from flask import Flask, jsonify

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
    for figure in possible_figures_mapping:
        if figure == chess_figure:
            output["availableMoves"] = possible_figures_mapping[figure](
                chessboard.chess_Position_Str_To_Int_Touple(current_field.upper())).list_available_moves()
    if len(output["availableMoves"]) != 0:
        output["error"] = None
    else:
        output["error"] = "Field does not exist"
    output["figure"] = chess_figure
    output["currentField"] = current_field
    return jsonify(output)


if __name__ == '__main__':
    app.run()
