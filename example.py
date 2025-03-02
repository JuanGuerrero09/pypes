from pypes.liquids import Liquid
from pypes.materials import Material
from pypes.pipeline.pipeline import Pipeline

# Crear un líquido y un material
water = Liquid(name="Water", density=1000, viscosity=0.001)
steel = Material(name="Steel", youngs_modulus=2e11, roughness=0.00015)

# Crear una tubería
pipe = Pipeline(diameter=0.05, length=100, material=steel, fluid_velocity=3)

# Realizar cálculos
reynolds = pipe.calculate_reynolds(water.density, water.viscosity)
head_loss_value = pipe.calculate_head_loss(friction_factor=0.02)

print(f"Reynolds number: {reynolds}")
print(f"Head loss: {head_loss_value} meters")
