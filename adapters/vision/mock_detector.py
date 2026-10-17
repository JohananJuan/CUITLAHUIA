from datetime import datetime
from typing import List
import numpy as np

from core.domain.tomato import ObservacionTomate
from core.ports.detector_port import DetectorPort


class MockDetector(DetectorPort):

    def detectar(self, imagen: np.ndarray, id_planta: str) -> List[ObservacionTomate]:
        return [
            ObservacionTomate(
                fecha=datetime.now(),
                id_planta=id_planta,
                codigo_clase="green",
                nombre_clase="Verde",
                confianza=0.95,
                caja=(10, 20, 50, 60),
            ),
            ObservacionTomate(
                fecha=datetime.now(),
                id_planta=id_planta,
                codigo_clase="turning",
                nombre_clase="Cambiante",
                confianza=0.88,
                caja=(70, 30, 110, 80),
            ),
            ObservacionTomate(
                fecha=datetime.now(),
                id_planta=id_planta,
                codigo_clase="red",
                nombre_clase="Rojo",
                confianza=0.92,
                caja=(120, 40, 160, 90),
            ),
        ]