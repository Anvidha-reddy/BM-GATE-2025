import numpy as np

# ==============================================================================
#   - Carbon (a) = 6  (from TOC data)
#   - Nitrogen (d) = 2  (from TKN data)
#
# Total MW = 12(a) + 1(b) + 16(c) + 14(d) = 187
# Substitute a = 6, d = 2:
# 12(6) + b + 16c + 14(2) = 187
# 72 + b + 16c + 28 = 187  -->  b + 16c = 87

# From COD data (0.6 g/L O2 consumed), O2 required = 3.75 moles O2 / mole compound.
# Stoichiometric coefficient for O2: (4a + b - 2c - 3d) / 4 = 3.75
# Substitute a = 6, d = 2:
# (24 + b - 2c - 6) / 4 = 3.75
# 18 + b - 2c = 15  -->  b - 2c = -3

# ==============================================================================
# MATRIX FORMULATION: Ax = y
# [ 1   16 ] [ b ] = [ 87 ]
# [ 1   -2 ] [ c ]   [ -3 ]
# ==============================================================================

# Matrix of coefficients for variables [b, c]
A = np.array([
    [1, 16],  # Row 1: 1*b + 16*c
    [1, -2]   # Row 2: 1*b -  2*c
])

# Right-hand side values
y = np.array([87, -3])

# Solve for x = [b, c]
x = np.linalg.solve(A, y)

b = x[0]
c = x[1]

# Display results
print(f"Number of Hydrogen atoms (b): {b:.0f}")
print(f"Number of Oxygen atoms   (c): {c:.0f}")
