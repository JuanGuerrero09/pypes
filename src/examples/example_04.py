import math

from pypes.liquids import Liquid
from pypes.materials import Material
from pypes.pipeline import Pipeline
from pypes.reynolds import reynolds_number

crude_oil = Liquid("oil", 925, 0.065)
area = math.pi * 0.05**2
velocity = 0.01 / area
pipeline = Pipeline(
    diameter=0.1, fluid_velocity=velocity, length=1, material=Material("", 0, 0)
)
print(
    pipeline.calculate_reynolds(
        liquid_density=crude_oil.density, liquid_viscosity=crude_oil.viscosity
    )
)
