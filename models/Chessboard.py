import string


class Chessboard:
    def __init__(self):
        self.letters: list = list(string.ascii_uppercase[0:7])
        self.numbers: list = [number for number in range(1, 9)]
        self.fields: list = [str(number) + str(letter) for number, letter in zip(self.numbers, self.letters)]
