import math


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


def calculate_friction_factor(
    reynolds: float,
    diameter: float,
    roughness: float,
    tol: float = 1e-7,
    max_iter: int = 100,
):
    k = roughness
    D = diameter
    Re = reynolds

    # Función de la ecuación de Colebrook-White
    def colebrook_equation(f):
        left = 1 / math.sqrt(f)
        right = -2 * math.log10((k / (3.7 * D)) + (2.51 / (Re * math.sqrt(f))))
        return left - right

    # Inicialización de los valores iniciales para el factor de fricción
    fa = 0.0001  # Valor inicial bajo
    fb = 0.1  # Valor inicial alto

    # Verificación de que los valores iniciales tienen signos opuestos
    if colebrook_equation(fa) * colebrook_equation(fb) >= 0:
        raise ValueError(
            "Los valores iniciales fa y fb no tienen signos opuestos. Ajusta los valores iniciales."
        )

    # Método de bisección
    for i in range(max_iter):
        fc = (fa + fb) / 2
        fc_value = colebrook_equation(fc)

        if abs(fc_value) < tol:
            return fc

        if colebrook_equation(fa) * fc_value < 0:
            fb = fc
        else:
            fa = fc

    raise ValueError(
        "El método de bisección no convergió después de {} iteraciones.".format(
            max_iter
        )
    )


# Ejemplo de uso
reynolds = 100000
diameter = 0.1
roughness = 0.00015

friction_factor = calculate_friction_factor(reynolds, diameter, roughness)
print(f"El factor de fricción es: {friction_factor}")
