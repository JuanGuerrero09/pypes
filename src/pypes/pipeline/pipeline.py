import math

from pypes.liquids import WATER, Liquid
from pypes.materials import CARBON_STEEL, Material
from pypes.pipeline.calculations import (
    calculate_friction_factor,
    head_loss,
    reynolds_number,
)


class Pipeline:
    def __init__(
        self,
        diameter: float,
        material: Material = CARBON_STEEL,
        length: float = 1,
        flow: float = 0,
        fluid: Liquid = WATER,
    ):
        """
        Represents a pipeline with relevant properties.

        :param diameter: Pipe diameter in milimeters.
        :param length: Pipe length in meters.
        :param material: Material of the pipeline (instance of Material, default is Carbon Steel).
        :param flow: Flow along the pipeline in cubic meters per second.
        """
        self.diameter = diameter
        self.length = length
        self.material = material
        self.flow = flow
        self.fluid = fluid

    def calculate_pipe_friction_factor(self) -> float:
        Re = self.calculate_reynolds()
        D = self.diameter
        e = self.material.roughness

        return calculate_friction_factor(reynolds=Re, diameter=D, roughness=e)

    def calculate_reynolds(
        self,
    ) -> float:
        """
        Calculates the Reynolds number for this pipeline.
        """
        return reynolds_number(
            viscosity=self.fluid.viscosity,
            density=self.fluid.density,
            velocity=self.calculate_velocity(),
            diameter=self.diameter,
        )

    def calculate_area(self) -> float:
        area = math.pi * self.diameter**2 / 4
        return area

    def calculate_velocity(self) -> float:
        area = self.calculate_area()
        return self.flow / area

    def calculate_head_loss(self) -> float:
        """
        Calculates head loss in the pipeline.
        """
        return head_loss(
            self.calculate_pipe_friction_factor(),
            self.length,
            self.diameter,
            self.calculate_velocity(),
        )

    def __repr__(self):
        return (
            f"Pipeline(diameter={self.diameter}, length={self.length}, "
            f"material={self.material}, flow={self.flow})"
        )
