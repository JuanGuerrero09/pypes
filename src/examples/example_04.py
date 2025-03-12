import math

from pypes.liquids import Liquid
from pypes.materials import Material
from pypes.pipeline import Pipeline
from pypes.pipeline.calculations import calculate_friction_factor
from pypes.reynolds import reynolds_number

crude_oil = Liquid("oil", 925, 0.065)
area = math.pi * 0.05**2
pipeline = Pipeline(diameter=0.1, flow=0.01, length=1, fluid=crude_oil)
print(pipeline.calculate_reynolds())

f = calculate_friction_factor(reynolds=3.45 * 10**5, roughness=0.03, diameter=200)
print(f)
