from abc import ABC, abstractmethod
from typing import List
import numpy as np

from core.domain.tomato import ObservacionTomate


class DetectorPort(ABC):

    @abstractmethod
    def detectar(self, imagen: np.ndarray, id_planta: str) -> List[ObservacionTomate]:
        ...