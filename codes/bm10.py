import os
import shutil
import subprocess
import shlex

import numpy as np
import matplotlib.pyplot as plt

# Import custom matrix and vector modules
from CoordGeo.line.funcs import line_gen_num

# Initialize figure
fig, ax = plt.subplots(figsize=(10, 5), layout='constrained')

# Time axis (0 to 0.1 s) generated as points on a line;
# the same points also draw the zero axis
A_ax = np.array([0.0, 0.0]).reshape(-1, 1)
B_ax = np.array([0.1, 0.0]).reshape(-1, 1)
x_ax = line_gen_num(A_ax, B_ax, 5000)
t = x_ax[0, :]

# Given signal
x = (20 * np.sin(100 * np.pi * t)
     + 36 * np.sin(150 * np.pi * t)
     - 2 * np.sin(300 * np.pi * t))

# Plot
ax.plot(t, x, 'b-', linewidth=1.5,
        label=r'$x(t)=20\sin(100\pi t)+36\sin(150\pi t)-2\sin(300\pi t)$')
ax.plot(x_ax[0, :], x_ax[1, :], 'k--', linewidth=0.8)

# Formatting plot area
ax.set_xlim(0, 0.1)
ax.grid(True, linestyle='--', alpha=0.5)

# Remove the outer plot box (spines)
for spine in ax.spines.values():
    spine.set_visible(False)

# Axis labels
ax.set_xlabel('t (seconds)')
ax.set_ylabel('x(t)')

# Legend
ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0., frameon=True)

# Save figure (run from repo root: python3 codes/bm10.py)
os.makedirs('figs', exist_ok=True)
plt.savefig('figs/bm10.png', dpi=150)

# Open the image: termux-open on phone, normal window on laptop/PC
if shutil.which('termux-open'):
    subprocess.run(shlex.split("termux-open figs/bm10.png"))
else:
    plt.show()
