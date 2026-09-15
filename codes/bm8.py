import matplotlib.pyplot as plt
import numpy as np

# 1. Define x domain (excluding 0)
x = np.linspace(0.2, 3.0, 400)

# 2. Define function and derivative equations
f_x = x - 1 / x
f_prime = 1 + 1 / (x**2)

# 3. Tangent point values at x = 1
x0 = 1.0
y0 = x0 - 1 / x0
slope = 1 + 1 / (x0**2)
tangent_y = slope * (x - x0) + y0

# Create tall figure with 2 vertical subplots (stacked up and down)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# --- Subplot 1: Derivative Plot (Top) ---
ax1.plot(
    x,
    f_prime,
    color="purple",
    linewidth=2.5,
    label=r"$f'(x) = 1 + \frac{1}{x^2}$",
)
ax1.scatter([x0], [slope], color="red", zorder=5, s=80)
ax1.annotate(
    f"f'(1) = {slope:.0f}\n(1, 2)",
    (x0, slope),
    textcoords="offset points",
    xytext=(-35, 15),
    fontsize=11,
    fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="black", lw=1.5),
)

ax1.set_title(
    r"Derivative Graph $f'(x)$", fontsize=14, fontweight="bold", pad=10
)
ax1.set_xlabel("x", fontsize=12)
ax1.set_ylabel("f'(x)", fontsize=12)
ax1.grid(True, linestyle=":", alpha=0.6)
ax1.legend(fontsize=11)

# --- Subplot 2: Function & Tangent Line Plot (Bottom) ---
ax2.plot(x, f_x, color="blue", linewidth=2.5, label=r"$f(x) = x - \frac{1}{x}$")
ax2.plot(
    x,
    tangent_y,
    color="red",
    linestyle="--",
    linewidth=2.5,
    label=r"Tangent: $y = 2x - 2$",
)

# Mark point (x, y) = (1, 0) for tangent
ax2.scatter([x0], [y0], color="black", zorder=5, s=80)
ax2.annotate(
    f"Point of Tangency\n(x={x0:.0f}, y={y0:.0f})",
    (x0, y0),
    textcoords="offset points",
    xytext=(30, -30),
    fontsize=11,
    fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="black", lw=1.5),
)

# Dotted reference lines to axes
ax2.vlines(
    x=x0, ymin=min(f_x), ymax=y0, color="gray", linestyle=":", linewidth=1.5
)
ax2.hlines(
    y=y0, xmin=min(x), xmax=x0, color="gray", linestyle=":", linewidth=1.5
)

ax2.set_title(
    r"Function $f(x)$ & Tangent at $x=1$",
    fontsize=14,
    fontweight="bold",
    pad=10,
)
ax2.set_xlabel("x", fontsize=12)
ax2.set_ylabel("y", fontsize=12)
ax2.axhline(0, color="black", linewidth=0.8)
ax2.axvline(0, color="black", linewidth=0.8)
ax2.grid(True, linestyle=":", alpha=0.6)
ax2.legend(fontsize=11)

plt.tight_layout(pad=2.5)
plt.savefig("bm8a.png", dpi=300)
plt.close()
