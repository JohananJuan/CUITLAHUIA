from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ClaseTomate:
    codigo: str
    nombre_espanol: str
    porcentaje_rojo_min: float
    porcentaje_rojo_max: float


@dataclass(frozen=True)
class ObservacionTomate:
    fecha: datetime
    id_planta: str
    codigo_clase: str
    nombre_clase: str
    confianza: float
    caja: tuple[int, int, int, int] 