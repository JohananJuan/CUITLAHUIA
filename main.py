from datetime import datetime
import numpy as np

from core.ports.detector_port import DetectorPort
from core.ports.repository_port import RepositorioPort
from core.services.classification_service import ServicioClasificacion


def procesar_imagen(
    imagen: np.ndarray,
    id_planta: str,
    detector: DetectorPort,
    repositorio: RepositorioPort,
    servicio: ServicioClasificacion,
) -> None:
    print(f"Procesando planta {id_planta}...")

    observaciones = detector.detectar(imagen, id_planta)
    if not observaciones:
        print("  No se detectaron tomates.")
        return

    conteo = servicio.agrupar(observaciones)
    print(f"  Detecciones: {len(observaciones)}")
    print(f"  Agrupación: {conteo}")

    repositorio.guardar(observaciones)
    print("  Observaciones guardadas.")


def main() -> None:
    from adapters.vision.mock_detector import MockDetector
    from adapters.persistence.csv_repository import CsvRepositorio

    detector = MockDetector()
    repositorio = CsvRepositorio(ruta="data/observaciones.csv")
    servicio = ServicioClasificacion()

    imagen_falsa = np.zeros((480, 640, 3), dtype=np.uint8)

    procesar_imagen(
        imagen=imagen_falsa,
        id_planta="JT-001",
        detector=detector,
        repositorio=repositorio,
        servicio=servicio,
    )


if __name__ == "__main__":
    main()