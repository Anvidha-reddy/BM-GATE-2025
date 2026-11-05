import numpy as np

n = 2  # Two-lane highway
l = 7.0  # Wheelbase in m
R = 300.0  # Radius in m
V = 80.0  # Design speed in km/h

# Mechanical and psychological widening
Wm = (n * l**2) / (2 * R)
Wp = V / (9.5 * np.sqrt(R))
We = Wm + Wp

print(f"Extra widening required: {We:.2f} m")
