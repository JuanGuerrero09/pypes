def reynolds_number(
    density: float, velocity: float, diameter: float, viscosity: float
) -> float:
    """
    Calculates the Reynolds number.

    :param density: Fluid density in kg/m³
    :param velocity: Fluid velocity in m/s
    :param diameter: Pipe diameter in meters
    :param viscosity: Absolute viscosity in Pa·s
    :return: Reynolds number
    """
    return (density * velocity * diameter) / viscosity


def head_loss(
    friction_factor: float, length: float, diameter: float, velocity: float
) -> float:
    """
    Calculates the head loss in a pipeline using the Darcy-Weisbach equation.

    :param friction_factor: Dimensionless friction factor
    :param length: Length of the pipe in meters
    :param diameter: Pipe diameter in meters
    :param velocity: Fluid velocity in meters per second
    :return: Head loss in meters
    """
    g = 9.81  # Acceleration due to gravity in m/s²
    return (friction_factor * (length / diameter) * (velocity**2)) / (2 * g)
