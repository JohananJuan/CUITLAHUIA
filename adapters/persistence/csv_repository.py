import csv
from datetime import datetime
from pathlib import Path
from typing import List

from core.domain.tomato import ObservacionTomate
from core.ports.repository_port import RepositorioPort


class CsvRepositorio(RepositorioPort):

    ENCABEZADOS = [
        "fecha", "id_planta", "codigo_clase",
        "nombre_clase", "confianza", "x1", "y1", "x2", "y2"
    ]

    def __init__(self, ruta: str = "data/observaciones.csv"):
        self.ruta = Path(ruta)
        self.ruta.parent.mkdir(parents=True, exist_ok=True)

    def guardar(self, observaciones: List[ObservacionTomate]) -> None:
        archivo_existe = self.ruta.exists()
        modo = "a" if archivo_existe else "w"

        with open(self.ruta, mode=modo, newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not archivo_existe:
                writer.writerow(self.ENCABEZADOS)

            for obs in observaciones:
                writer.writerow([
                    obs.fecha.isoformat(),
                    obs.id_planta,
                    obs.codigo_clase,
                    obs.nombre_clase,
                    f"{obs.confianza:.4f}",
                    obs.caja[0], obs.caja[1], obs.caja[2], obs.caja[3],
                ])

    def leer_todas(self) -> List[ObservacionTomate]:
        if not self.ruta.exists():
            return []

        observaciones = []
        with open(self.ruta, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for fila in reader:
                observaciones.append(ObservacionTomate(
                    fecha=datetime.fromisoformat(fila["fecha"]),
                    id_planta=fila["id_planta"],
                    codigo_clase=fila["codigo_clase"],
                    nombre_clase=fila["nombre_clase"],
                    confianza=float(fila["confianza"]),
                    caja=(int(fila["x1"]), int(fila["y1"]),
                          int(fila["x2"]), int(fila["y2"])),
                ))
        return observaciones