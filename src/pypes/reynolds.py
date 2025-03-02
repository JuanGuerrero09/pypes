# Function to calculate Reynolds number
def reynolds_number(
    density: float, velocity: float, diameter: float, viscosity: float
) -> float:
    """
    Calculate Reynolds number.

    Parameters:
    density (float): Fluid density (kg/m³)
    velocity (float): Flow velocity (m/s)
    diameter (float): Pipe diameter (m)
    viscosity (float): Dynamic viscosity (Pa·s)

    Returns:
    float: Reynolds number
    """
    return (density * velocity * diameter) / viscosity
