import os
import shutil
import subprocess
import shlex

import numpy as np
import matplotlib.pyplot as plt

# Import custom matrix and vector modules
from CoordGeo.line.funcs import line_gen, line_gen_num, line_dir_pt
from CoordGeo.plotting.funcs import label_pts

# Initialize figure with 2 vertical subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), layout='constrained')

# 1. Domain of x (excluding 0), generated as points on a line
A_dom = np.array([0.2, 0.0]).reshape(-1, 1)
B_dom = np.array([3.0, 0.0]).reshape(-1, 1)
x = line_gen_num(A_dom, B_dom, 400)[0, :]

# 2. Function and derivative
f_x = x - 1 / x
f_prime = 1 + 1 / (x**2)

# 3. Point of tangency at x = 1
x0 = 1.0
y0 = x0 - 1 / x0                 # 0
slope = 1 + 1 / (x0**2)          # 2
P0 = np.array([x0, y0]).reshape(-1, 1)         # (1, 0) on f(x)
Q0 = np.array([x0, slope]).reshape(-1, 1)      # (1, 2) on f'(x)

# 4. Tangent line y = 2x - 2 in parametric form: point P0, direction m = (1, slope)
m = np.array([1.0, slope]).reshape(-1, 1)
x_tan = line_dir_pt(m, P0, x[0] - x0, x[-1] - x0)

# 5. Dotted reference lines from the point to the axes
P_x = np.array([x0, f_x.min()]).reshape(-1, 1)
P_y = np.array([x[0], y0]).reshape(-1, 1)
x_vref = line_gen(P_x, P0)
x_href = line_gen(P_y, P0)

# --- Subplot 1: Derivative plot (top) ---
ax1.plot(x, f_prime, color='purple', linewidth=2.5,
         label=r"$f'(x) = 1 + \frac{1}{x^2}$")
ax1.scatter(Q0[0, 0], Q0[1, 0], color='red', zorder=5, s=80)
plt.sca(ax1)
label_pts(Q0, ["f'(1) = 2\n(1, 2)"])

ax1.set_title(r"Derivative Graph $f'(x)$", fontsize=14, fontweight='bold')
ax1.set_xlabel('x')
ax1.set_ylabel("f'(x)")
ax1.grid(True, linestyle='--', alpha=0.5)
for spine in ax1.spines.values():
    spine.set_visible(False)
ax1.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0., frameon=True)

# --- Subplot 2: Function and tangent line (bottom) ---
ax2.plot(x, f_x, color='blue', linewidth=2.5, label=r'$f(x) = x - \frac{1}{x}$')
ax2.plot(x_tan[0, :], x_tan[1, :], color='red', linestyle='--', linewidth=2.5,
         label=r'Tangent: $y = 2x - 2$')
ax2.plot(x_vref[0, :], x_vref[1, :], color='gray', linestyle=':', linewidth=1.5)
ax2.plot(x_href[0, :], x_href[1, :], color='gray', linestyle=':', linewidth=1.5)
ax2.scatter(P0[0, 0], P0[1, 0], color='black', zorder=5, s=80)
plt.sca(ax2)
label_pts(P0, ['Point of Tangency\n(1, 0)'])

ax2.set_title(r'Function $f(x)$ & Tangent at $x=1$', fontsize=14, fontweight='bold')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.axhline(0, color='black', linewidth=0.8)
ax2.axvline(0, color='black', linewidth=0.8)
ax2.grid(True, linestyle='--', alpha=0.5)
for spine in ax2.spines.values():
    spine.set_visible(False)
ax2.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0., frameon=True)

# Save figure (run from repo root: python3 codes/bm8.py)
os.makedirs('figs', exist_ok=True)
plt.savefig('figs/bm8a.png', dpi=300)

# Open the image: termux-open on phone, normal window on laptop/PC
if shutil.which('termux-open'):
    subprocess.run(shlex.split("termux-open figs/bm8a.png"))
else:
    plt.show()
