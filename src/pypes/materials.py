from dataclasses import dataclass


@dataclass
class Material:
    """Clase que representa un material de tubería con sus propiedades."""

    name: str
    youngs_modulus: float  # Módulo de Young (Pa)
    roughness: float  # Rugosidad en metros


# Default Materials

CARBON_STEEL = Material(name="Carbon Steel", roughness=0.05, youngs_modulus=2e11)
