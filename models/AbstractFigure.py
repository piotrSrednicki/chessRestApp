from abc import ABC, abstractmethod
from typing import Tuple

class Figure(ABC):
    def __init__(self, field: Tuple[int, int]):
        self.field = field

    @abstractmethod
    def list_available_moves(self) -> None:
        pass

    @abstractmethod
    def validate_move(self, dest_field: Tuple[int, int]) -> None:
        pass
