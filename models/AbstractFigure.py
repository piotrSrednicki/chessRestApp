from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, field: tuple[int, int]):
        pass

    @abstractmethod
    def list_available_moves(self) -> None:
        pass

    @abstractmethod
    def validate_move(self, dest_field: tuple[int, int]) -> None:
        pass
