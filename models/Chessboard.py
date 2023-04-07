import itertools
import string

from typing import Tuple

class Chessboard:
    def __init__(self):
        self.letters: list[str] = list(string.ascii_uppercase[0:8])
        self.numbers: list[int] = [number for number in range(1, 9)]
        self.fields: list[str] = [
            str(letter) + str(number)
            for number, letter in list(
                itertools.product(self.numbers, self.letters)
            )
        ]

    def int_Touple_To_Chess_PositionStr(
        self, x_y_position: Tuple[int, int]
    ) -> str:
        return self.letters[x_y_position[0]] + str(
            self.numbers[x_y_position[1]]
        )

    def chess_Position_Str_To_Int_Touple(
        self, chess_position: str
    ) -> Tuple[int, int]:
        if len(chess_position) != 2:
            return -1, -1
        for index, letter in enumerate(self.letters):
            if letter == chess_position[0]:
                try:
                    return index, int(chess_position[1]) - 1
                except Exception:
                    return -1,-1
