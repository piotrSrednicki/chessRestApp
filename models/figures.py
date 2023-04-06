from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, field):
        pass

    @abstractmethod
    def list_available_moves(self) -> list[tuple]:
        pass

    def validate_move(self, dest_field: tuple):
        pass
