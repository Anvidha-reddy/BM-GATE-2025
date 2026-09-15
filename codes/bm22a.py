import matplotlib.pyplot as plt
import numpy as np

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

# 3. Data for Plotting
x = np.linspace(0.5, 3.5, 500)
y = f(x)

fig, ax = plt.subplots(figsize=(10, 6))

# Plot curve f(x) and zero line
ax.plot(
    x, y, label=r"$f(x) = x^3 - 2x - 5$", color="navy", linewidth=2.5
)
ax.axhline(0, color="black", linestyle="--", linewidth=1.2)

# Tangent line at x0 = 3 (Slope m = f'(3) = 25)
x_tangent = np.linspace(1.8, 3.3, 100)
y_tangent = df(x0) * (x_tangent - x0) + f(x0)
ax.plot(
    x_tangent,
    y_tangent,
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

# Formatting

ax.set_xlabel("$x$", fontsize=12)
ax.set_ylabel("$f(x)$", fontsize=12)
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend(fontsize=11)

# Save plot relative to script location
plt.tight_layout()
plt.savefig("bm22a.png", dpi=300)
plt.close()

