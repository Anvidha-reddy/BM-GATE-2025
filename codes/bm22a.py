import os
import shutil
import subprocess
import shlex

import numpy as np
import matplotlib.pyplot as plt

# Import custom matrix and vector modules
from CoordGeo.line.funcs import line_gen_num

# 1. Function, Derivative, and Explicit Update Formula
def f(x):
    return x**3 - 2 * x - 5

def df(x):
    return 3 * x**2 - 2

def update_eq(x):
    return (2 * x**3 + 5) / (3 * x**2 - 2)

# 2. Compute Iterations
x0 = 3.0
x1 = update_eq(x0)  # 2.36

# Convergence to find exact root
x_curr = x0
for _ in range(10):
    x_curr = update_eq(x_curr)
root = x_curr

print(f"Initial Guess (x0): {x0}")
print(f"First Iteration (x1): {x1:.2f}")
print(f"Converged Real Root: {root:.4f}")

# Initialize figure
fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')

# 3. x axis (0.5 to 3.5) generated as points on a line;
#    the same points also draw the zero line
A_ax = np.array([0.5, 0.0]).reshape(-1, 1)
B_ax = np.array([3.5, 0.0]).reshape(-1, 1)
x_ax = line_gen_num(A_ax, B_ax, 500)
x = x_ax[0, :]
y = f(x)

# Plot curve f(x) and zero line
ax.plot(
    x, y, label=r"$f(x) = x^3 - 2x - 5$", color="navy", linewidth=2.5
)
ax.plot(x_ax[0, :], x_ax[1, :], 'k--', linewidth=1.2)

# Tangent line at x0 = 3 (Slope m = f'(3) = 25) using line points
T1 = np.array([1.8, df(x0) * (1.8 - x0) + f(x0)]).reshape(-1, 1)
T2 = np.array([3.3, df(x0) * (3.3 - x0) + f(x0)]).reshape(-1, 1)
x_tan = line_gen_num(T1, T2, 100)
ax.plot(
    x_tan[0, :],
    x_tan[1, :],
    color="red",
    linestyle="--",
    linewidth=1.5,
    label=r"Tangent line at $x_0=3$ (Slope = 25)",
)

# Plot Points
ax.scatter([x0], [f(x0)], color="red", zorder=5, s=80)
ax.scatter([x1], [0], color="green", zorder=5, s=80, label=r"$x_1 = 2.36$")
ax.scatter(
    [root],
    [0],
    color="purple",
    zorder=5,
    s=80,
    label=rf"Actual Root $\alpha \approx {root:.4f}$",
)

# Annotations
ax.annotate(
    r"$(x_0, f(x_0)) = (3, 16)$",
    (x0, f(x0)),
    textcoords="offset points",
    xytext=(-120, -5),
    fontsize=10,
    fontweight="bold",
    color="red",
)
ax.annotate(
    r"$x_1 = 2.36$",
    (x1, 0),
    textcoords="offset points",
    xytext=(-25, 15),
    fontsize=10,
    fontweight="bold",
    color="green",
)
ax.annotate(
    rf"Root $\approx {root:.4f}$",
    (root, 0),
    textcoords="offset points",
    xytext=(-50, -20),
    fontsize=10,
    fontweight="bold",
    color="purple",
)

# Formatting plot area
ax.grid(True, linestyle=':', alpha=0.6)

# Remove the outer plot box (spines)
for spine in ax.spines.values():
    spine.set_visible(False)

# Axis labels
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')

# Legend
ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0., frameon=True)

# Save figure (run from repo root: python3 codes/bm22a.py)
os.makedirs('figs', exist_ok=True)
plt.savefig('figs/bm22a.png', dpi=300)

# Open the image: termux-open on phone, normal window on laptop/PC
if shutil.which('termux-open'):
    subprocess.run(shlex.split("termux-open figs/bm22a.png"))
else:
    plt.show()
