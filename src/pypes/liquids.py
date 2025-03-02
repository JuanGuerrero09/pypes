from dataclasses import dataclass


@dataclass
class Liquid:
    """Clase que representa un líquido con sus propiedades."""

    name: str
    density: float  # Densidad en kg/m³
    viscosity: float  # Viscosidad en Pa·s
