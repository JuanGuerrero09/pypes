import pytest

from pypes.head_loss import head_loss
from pypes.reynolds import reynolds_number


def test_reynolds_number():
    # Sample test data (density = 1000 kg/m³, velocity = 3 m/s, diameter = 0.05 m, viscosity = 0.001 Pa·s)
    result = reynolds_number(1000, 3, 0.05, 0.001)
    assert result == 150000.0  # Expected Reynolds number


def test_head_loss():
    # Sample test data (friction_factor = 0.02, length = 100 m, diameter = 0.05 m, velocity = 3 m/s)
    result = head_loss(0.02, 100, 0.05, 3)
    assert result == 36.0  # Expected head loss in meters


# def test_head_loss_invalid():
#     with pytest.raises(ValueError):
#         head_loss(-0.02, 100, 0.05, 3)  # Negative friction factor should raise an error
