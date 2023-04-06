import pytest

from models.Chessboard import Chessboard


@pytest.fixture
def chessboard():
    return Chessboard()


def test_if_chessboard_has_64_fields(chessboard):
    assert len(chessboard.fields) == 64


def test_if_chessboard_has_correct_letters_list(chessboard):
    assert len(chessboard.numbers) == 8
    assert chessboard.numbers == [1, 2, 3, 4, 5, 6, 7, 8]


def test_if_chessboard_has_correct_numbers_list(chessboard):
    assert len(chessboard.letters) == 8
    assert chessboard.letters == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
