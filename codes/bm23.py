import os
import shutil
import subprocess
import shlex

import numpy as np
import matplotlib.pyplot as plt

# Import custom matrix and vector modules
from CoordGeo.line.funcs import line_gen_num

# Initialize figure
fig, ax = plt.subplots(figsize=(8, 5), layout='constrained')

# Given condition
sigma0 = 2 + 2*np.log(4)

# Time in weeks generated as points on a line
A_ax = np.array([1.0, 0.0]).reshape(-1, 1)
B_ax = np.array([12.0, 0.0]).reshape(-1, 1)
x_ax = line_gen_num(A_ax, B_ax, 500)
t = x_ax[0, :]

# Strength equation
sigma = sigma0 - 2*np.log(t)

# Plot
ax.plot(t, sigma, 'b-', linewidth=2, label=r'$\sigma=\sigma_0-2\ln t$')

# Mark the given point (4, 2)
ax.plot(4, 2, 'ro', label='(4, 2)')

# Mark the strength at 8 weeks
sigma8 = sigma0 - 2*np.log(8)
ax.plot(8, sigma8, 'go', label=f'(8, {sigma8:.3f})')

# Formatting plot area
ax.grid(True, linestyle=':', alpha=0.6)

# Remove the outer plot box (spines)
for spine in ax.spines.values():
    spine.set_visible(False)

# Axis labels
ax.set_xlabel("Time (weeks)")
ax.set_ylabel("Strength (MPa)")

# Legend
ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0., frameon=True)

# Save figure (run from repo root: python3 codes/bm23.py)
os.makedirs('figs', exist_ok=True)
plt.savefig('figs/bm23.png', dpi=300)

# Open the image: termux-open on phone, normal window on laptop/PC
if shutil.which('termux-open'):
    subprocess.run(shlex.split("termux-open figs/bm23.png"))
else:
    plt.show()
