from models.AbstractFigure import Figure
from models.Chessboard import Chessboard


class QueenFigure(Figure):
    def __init__(self, field: tuple[int, int]):
        super().__init__(field)
        self.field = field
        # top-left, top, top-right...
        # x - abcd
        # y - 1234
        self.moves_list: list[(int, int)] = [(0, x) for x in range(-7, 8) if x != 0] + \
                                            [(x, 0) for x in range(-7, 8) if x != 0] + [(x, y) for x, y in
                                                                                        zip(range(-7, 8), range(-7, 8))
                                                                                        if x != 0 and y != 0] \
                                            + [(x, y) for x, y in
                                               zip(range(-7, 8), reversed(range(-7, 8)))
                                               if x != 0 and y != 0]
        self.min_x_and_y: int = 0
        self.max_x_and_y: int = 7
        self.chessboard: Chessboard = Chessboard()

    def list_available_moves(self) -> list[str]:
        assert self.field[0] in range(self.min_x_and_y, self.max_x_and_y + 1) \
               and self.field[1] in range(self.min_x_and_y, self.max_x_and_y + 1)
        available_moves: list[str] = []
        for move in self.moves_list:
            position_after_move: tuple[int, int] = self.field[0] + move[0], self.field[1] + move[1]
            if position_after_move[0] in range(self.min_x_and_y, self.max_x_and_y + 1) \
                    and position_after_move[1] in range(self.min_x_and_y, self.max_x_and_y + 1):
                available_moves.append(self.chessboard.int_Touple_To_Chess_PositionStr(position_after_move))
        return available_moves

    def validate_move(self, dest_field: tuple) -> str:
        possible_moves = self.list_available_moves()
        print(dest_field, possible_moves)
        if self.chessboard.int_Touple_To_Chess_PositionStr(dest_field) in possible_moves:
            return "valid"
        return "invalid"
