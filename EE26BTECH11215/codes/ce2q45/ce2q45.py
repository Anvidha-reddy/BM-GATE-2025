import numpy as np

A = np.array([
    [6, 8],
    [4, 2]
])
eigenvalues = np.linalg.eigvals(A)
print(f"Eigenvalues: {eigenvalues}")
