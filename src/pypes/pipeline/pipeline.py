import math

from pypes.materials import CARBON_STEEL, Material
from pypes.pipeline.calculations import head_loss, reynolds_number


class Pipeline:
    def __init__(
        self,
        diameter: float,
        material: Material = CARBON_STEEL,
        length: float = 1,
        flow: float = 0,
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
        self.flow = flow

    def calculate_reynolds(
        self, liquid_density: float, liquid_viscosity: float
    ) -> float:
        """
        Calculates the Reynolds number for this pipeline.
        """
        return reynolds_number(
            liquid_density, self.calculate_velocity(), self.diameter, liquid_viscosity
        )

    def calculate_area(self) -> float:
        area = math.pi * self.diameter**2 / 4
        return area

    def calculate_velocity(self) -> float:
        area = self.calculate_area()
        return self.flow / area

    def calculate_head_loss(self, friction_factor: float) -> float:
        """
        Calculates head loss in the pipeline.
        """
        return head_loss(
            friction_factor, self.length, self.diameter, self.calculate_velocity()
        )

    def __repr__(self):
        return (
            f"Pipeline(diameter={self.diameter}, length={self.length}, "
            f"material={self.material}, flow={self.flow})"
        )
