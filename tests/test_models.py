import pytest

from models.BishopFigure import BishopFigure
from models.Chessboard import Chessboard
from models.KingFigure import KingFigure
from models.KnightFigure import KnightFigure
from models.PawnFigure import PawnFigure
from models.QueenFigure import QueenFigure
from models.RookFigure import RookFigure


@pytest.fixture
def chessboard():
    return Chessboard()


def test_if_chessboard_has_64_fields(chessboard):
    assert len(chessboard.fields) == 64


def test_if_chessboard_has_correct_numbers_list(chessboard):
    assert len(chessboard.numbers) == 8
    assert chessboard.numbers == [1, 2, 3, 4, 5, 6, 7, 8]


def test_if_chessboard_has_correct_letters_list(chessboard):
    assert len(chessboard.letters) == 8
    assert chessboard.letters == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def test_if_rook_figure_lists_available_moves_correctly(chessboard):
    rookFigure = RookFigure((1, 1))
    assert rookFigure.list_available_moves() == ['B1', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'A2', 'C2', 'D2', 'E2', 'F2',
                                                 'G2', 'H2']


def test_if_rook_figure_lists_available_moves_correctly_negative(chessboard):
    rookFigure = RookFigure((1, 1))
    with pytest.raises(Exception) as exception:
        assert rookFigure.list_available_moves() == []


def test_if_rook_figure_validates_a_move_correctly(chessboard):
    rookFigure = RookFigure((1, 1))
    assert rookFigure.validate_move((1, 5)) == "valid"


def test_if_rook_figure_validates_a_move_correctly_reverse_negative(chessboard):
    rookFigure = RookFigure((1, 1))
    with pytest.raises(Exception) as exception:
        assert rookFigure.validate_move((2, 2)) == "valid"


def test_if_pawn_figure_lists_available_moves_correctly(chessboard):
    pawnFigure = PawnFigure((1, 1))
    print(pawnFigure.list_available_moves())
    assert pawnFigure.list_available_moves() == ["B3","B1"]


def test_if_pawn_figure_lists_available_moves_correctly_negative(chessboard):
    pawnFigure = PawnFigure((1, 1))
    with pytest.raises(Exception) as exception:
        assert pawnFigure.list_available_moves() == []


def test_if_pawn_figure_validates_a_move_correctly(chessboard):
    pawnFigure = PawnFigure((1, 1))
    assert pawnFigure.validate_move((1, 2)) == "valid"


def test_if_pawn_figure_validates_a_move_correctly_reverse_negative(chessboard):
    pawnFigure = PawnFigure((1, 1))
    with pytest.raises(Exception) as exception:
        assert pawnFigure.validate_move((2, 2)) == "valid"

def test_if_knight_figure_lists_available_moves_correctly(chessboard):
    knightFigure = KnightFigure((1, 1))
    print(knightFigure.list_available_moves())
    assert knightFigure.list_available_moves() == ['E1', 'E3', 'C5', 'A5']


def test_if_knight_figure_lists_available_moves_correctly_negative(chessboard):
    knightFigure = KnightFigure((1, 1))
    with pytest.raises(Exception) as exception:
        assert knightFigure.list_available_moves() == []


def test_if_knight_figure_validates_a_move_correctly(chessboard):
    knightFigure = KnightFigure((1, 1))
    assert knightFigure.validate_move((4, 2)) == "valid"


def test_if_knight_figure_validates_a_move_correctly_reverse_negative(chessboard):
    knightFigure = KnightFigure((1, 1))
    with pytest.raises(Exception) as exception:
        assert knightFigure.validate_move((2, 2)) == "valid"

def test_if_queen_figure_lists_available_moves_correctly(chessboard):
    queenFigure = QueenFigure((7, 7))
    print(queenFigure.list_available_moves())
    assert queenFigure.list_available_moves() == ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7']



def test_if_queen_figure_lists_available_moves_correctly_negative(chessboard):
    queenFigure = QueenFigure((1,1))
    with pytest.raises(Exception) as exception:
        assert queenFigure.list_available_moves() == []


def test_if_queen_figure_validates_a_move_correctly(chessboard):
    queenFigure = QueenFigure((1, 1))
    assert queenFigure.validate_move((3, 3)) == "valid"


def test_if_queen_figure_validates_a_move_correctly_reverse_negative(chessboard):
    queenFigure = QueenFigure((1, 1))
    with pytest.raises(Exception) as exception:
        assert queenFigure.validate_move((2, 3)) == "valid"

def test_if_king_figure_lists_available_moves_correctly(chessboard):
    kingFigure = KingFigure((1, 1))
    print(kingFigure.list_available_moves())
    assert kingFigure.list_available_moves() == ['A1', 'A2', 'A3', 'B1', 'B3', 'C1', 'C2', 'C3']



def test_if_king_figure_lists_available_moves_correctly_negative(chessboard):
    kingFigure = KingFigure((1,1))
    with pytest.raises(Exception) as exception:
        assert kingFigure.list_available_moves() == []


def test_if_king_figure_validates_a_move_correctly(chessboard):
    kingFigure = KingFigure((1, 1))
    assert kingFigure.validate_move((2, 2)) == "valid"


def test_if_king_figure_validates_a_move_correctly_reverse_negative(chessboard):
    kingFigure = KingFigure((1, 1))
    with pytest.raises(Exception) as exception:
        assert kingFigure.validate_move((2, 3)) == "valid"


def test_if_bishop_figure_lists_available_moves_correctly(chessboard):
    bishopFigure = BishopFigure((1, 1))
    print(bishopFigure.list_available_moves())
    assert bishopFigure.list_available_moves() == ['A1', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'A3', 'C1']




def test_if_bishop_figure_lists_available_moves_correctly_negative(chessboard):
    bishopFigure = BishopFigure((1,1))
    with pytest.raises(Exception) as exception:
        assert bishopFigure.list_available_moves() == []


def test_if_bishop_figure_validates_a_move_correctly(chessboard):
    bishopFigure = BishopFigure((1, 1))
    assert bishopFigure.validate_move((3, 3)) == "valid"


def test_if_bishop_figure_validates_a_move_correctly_reverse_negative(chessboard):
    bishopFigure = BishopFigure((1, 1))
    with pytest.raises(Exception) as exception:
        assert bishopFigure.validate_move((2, 3)) == "valid"

