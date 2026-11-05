import os
import shutil
import subprocess
import shlex

import numpy as np
import matplotlib.pyplot as plt

# Import custom matrix and vector modules
from CoordGeo.line.funcs import line_gen_num

# Initialize figure
fig, ax = plt.subplots(figsize=(9, 5), layout='constrained')

# Domain setup for clear stem visualization
x0, x_end = 0.0, 5.0
h = 0.2  # Step size
N = int(round((x_end - x0) / h)) + 1

# x grid generated as points on a line
A_ax = np.array([x0, 0.0]).reshape(-1, 1)
B_ax = np.array([x_end, 0.0]).reshape(-1, 1)
x = line_gen_num(A_ax, B_ax, N)[0, :]

# 1. Discrete Euler recurrence: y_{n+1} = 2*y_n - (1 - h^2/4)*y_{n-1}
y_rec = np.zeros(N)
y_rec[0] = 1.0        # Initial condition: y_0 = 1
y_rec[1] = 1.0 + h    # First forward step: y_1 = y_0 + h*v_0

for n in range(1, N - 1):
    y_rec[n + 1] = 2.0 * y_rec[n] - (1.0 - (h**2) / 4.0) * y_rec[n - 1]

# 2. Exact theoretical solution for comparison
y_exact = 1.5 * np.exp(0.5 * x) - 0.5 * np.exp(-0.5 * x)

# 3. Stem plot of the discrete Euler values y_n
markerline, stemlines, baseline = ax.stem(
    x, y_rec, linefmt='r-', markerfmt='ro', basefmt='k-',
    label=r'Euler Recurrence ($y_n$)',
)
plt.setp(stemlines, linewidth=1.5)
plt.setp(markerline, markersize=6)

# Overlay theoretical curve
ax.plot(x, y_exact, 'b--', linewidth=2,
        label=r'Theoretical $y(x) = 1.5e^{0.5x} - 0.5e^{-0.5x}$')

# Formatting plot area
ax.set_title(r'Euler Recurrence ($y_{n+1} = 2y_n - (1 - h^2/4)y_{n-1}$)')
ax.grid(True, linestyle='--', alpha=0.5)

# Remove the outer plot box (spines)
for spine in ax.spines.values():
    spine.set_visible(False)

# Axis labels
ax.set_xlabel('x')
ax.set_ylabel(r'$y_n$')

# Legend
ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0., frameon=True)

# Save figure (run from repo root: python3 codes/bm13.py)
os.makedirs('figs', exist_ok=True)
plt.savefig('figs/bm13.png', dpi=150)

# Open the image: termux-open on phone, normal window on laptop/PC
if shutil.which('termux-open'):
    subprocess.run(shlex.split("termux-open figs/bm13.png"))
else:
    plt.show()
