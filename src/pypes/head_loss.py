# Function to calculate head loss using Darcy-Weisbach equation
def head_loss(
    friction_factor: float, length: float, diameter: float, velocity: float
) -> float:
    """
    Calculate head loss due to friction in a pipe.

    Parameters:
    friction_factor (float): Darcy friction factor
    length (float): Pipe length (m)
    diameter (float): Pipe diameter (m)
    velocity (float): Flow velocity (m/s)

    Returns:
    float: Head loss (m)
    """
    return (friction_factor * length * velocity**2) / (2 * diameter)
