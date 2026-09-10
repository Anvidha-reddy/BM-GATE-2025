import sympy as sp

# Define the symbol for theta
theta = sp.symbols('theta', real=True)

# Define the matrix
A = sp.Matrix([
    [sp.cos(theta), -sp.sin(theta)],
    [sp.sin(theta),  sp.cos(theta)]
])

# Compute eigenvalues symbolically
eigenvalues = A.eigenvals()

print("Eigenvalues and their multiplicities:")
for val, count in eigenvalues.items():
    # Simplify the resulting expression using Euler's formula
    simplified_val = sp.rewrite(val, sp.exp)
    print(f"Eigenvalue: {val}  --> Simplified: {simplified_val}")
