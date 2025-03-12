from dataclasses import dataclass


@dataclass
class Liquid:
    """Clase que representa un líquido con sus propiedades."""

    name: str
    density: float  # Densidad en kg/m³
    viscosity: float  # Viscosidad en kg/m s


WATER = Liquid(name="Water", density=1000, viscosity=1.14 * 10e-3)
