import numpy as np

w = 6.25  # kN/m
L = 4.0  # m
total_load = w * L  # 25 kN

# Diameters of side and centre rods
d_side = 12.0  # mm
d_center = 30.0  # mm

# Stiffness ratio (proportional to d^2 since length and material are same)
stiffness_ratio = (d_center / d_side) ** 2  # 6.25

# Equilibrium and compatibility: 2 * R_B + R_D = 25, R_D = 6.25 * R_B
R_B = total_load / (2 + stiffness_ratio)
R_D = stiffness_ratio * R_B

print(f"Axial force in centre rod CD: {R_D:.1f} kN")
