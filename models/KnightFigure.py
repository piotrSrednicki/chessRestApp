from typing import List

from models.AbstractFigure import Figure


class KnightFigure(Figure):
    def __init__(self, field):
        super().__init__(field)

    def list_available_moves(self) -> List[str]:
        pass

    def validate_move(self, dest_field: tuple) -> tuple[str, str]:
        pass
