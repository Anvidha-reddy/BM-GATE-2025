import numpy as np

rho = 1000.0  # kg/m^3
g = 9.81  # m/s^2
b = 6.0  # m
M_P_target = 3924e3  # N.m

# Solving moment equation: M_P = rho * g * b * (25 * h / 2 - 100 / 3)
term = M_P_target / (rho * g * b)
h = (term + 100.0 / 3.0) * 2.0 / 25.0

print(f"Maximum water depth h: {round(h)} m")
