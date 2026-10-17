from abc import ABC, abstractmethod
from typing import List

from core.domain.tomato import ObservacionTomate


class RepositorioPort(ABC):

    @abstractmethod
    def guardar(self, observaciones: List[ObservacionTomate]) -> None:
        ...

    @abstractmethod
    def leer_todas(self) -> List[ObservacionTomate]:
        ...