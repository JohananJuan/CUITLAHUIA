from typing import Dict, List

from core.domain.tomato import ObservacionTomate


class ServicioClasificacion:
    GRUPOS: Dict[str, List[str]] = {
        "verde":  ["green", "breaker"],
        "pinton": ["turning"],
        "rojo":   ["pink", "light_red", "red"],
    }

    def agrupar(self, observaciones: List[ObservacionTomate]) -> Dict[str, int]:
        conteo = {grupo: 0 for grupo in self.GRUPOS}

        for obs in observaciones:
            for grupo, codigos in self.GRUPOS.items():
                if obs.codigo_clase in codigos:
                    conteo[grupo] += 1
                    break

        return conteo