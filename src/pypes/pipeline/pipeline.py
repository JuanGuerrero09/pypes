from pypes.materials import Material
from pypes.pipeline.calculations import head_loss, reynolds_number


class Pipeline:
    def __init__(
        self, diameter: float, length: float, material: Material, fluid_velocity: float
    ):
        """
        Represents a pipeline with relevant properties.

        :param diameter: Pipe diameter in meters.
        :param length: Pipe length in meters.
        :param material: Material of the pipeline (instance of Material).
        :param fluid_velocity: Flow velocity in meters per second.
        """
        self.diameter = diameter
        self.length = length
        self.material = material
        self.fluid_velocity = fluid_velocity

    def calculate_reynolds(
        self, liquid_density: float, liquid_viscosity: float
    ) -> float:
        """
        Calculates the Reynolds number for this pipeline.
        """
        return reynolds_number(
            liquid_density, self.fluid_velocity, self.diameter, liquid_viscosity
        )

    def calculate_head_loss(self, friction_factor: float) -> float:
        """
        Calculates head loss in the pipeline.
        """
        return head_loss(
            friction_factor, self.length, self.diameter, self.fluid_velocity
        )

    def __repr__(self):
        return (
            f"Pipeline(diameter={self.diameter}, length={self.length}, "
            f"material={self.material}, velocity={self.fluid_velocity})"
        )
