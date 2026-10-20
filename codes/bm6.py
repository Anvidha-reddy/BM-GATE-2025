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

# Parameters (closed loop: C(s)/R(s) = 25 / (s^2 + 5s + 25))
wn = 5.0
zeta = 0.5
sigma = zeta * wn                     # 2.5
wd = wn * np.sqrt(1 - zeta**2)        # 5*sqrt(3)/2
K = wn**2 / wd                        # 10/sqrt(3)

# 1. Time axis (0 to 3 s) generated as points on a line;
#    the same points also draw the zero axis
A_ax = np.array([0.0, 0.0]).reshape(-1, 1)
B_ax = np.array([3.0, 0.0]).reshape(-1, 1)
x_ax = line_gen_num(A_ax, B_ax, 1000)
t = x_ax[0, :]

# 2. Impulse response c(t) and decay envelope
c_t = K * np.exp(-sigma * t) * np.sin(wd * t)
env = K * np.exp(-sigma * t)

# Plot
ax.plot(t, c_t, 'b-', linewidth=2,
        label=r'$c(t)=\frac{10}{\sqrt{3}}e^{-\frac{5}{2}t}\sin\left(\frac{5\sqrt{3}}{2}t\right)$')
ax.plot(t, env, '--', color='red', alpha=0.5, label='Decay envelope')
ax.plot(t, -env, '--', color='red', alpha=0.5)
ax.plot(x_ax[0, :], x_ax[1, :], 'k--', linewidth=0.8)

# Formatting plot area
ax.set_title(r'Underdamped Impulse Response $c(t)$')
ax.set_xlim(0, 3)
ax.grid(True, linestyle=':', alpha=0.6)

# Remove the outer plot box (spines)
for spine in ax.spines.values():
    spine.set_visible(False)

# Axis labels
ax.set_xlabel('time (s)')
ax.set_ylabel('c(t)')

# Legend
ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0., frameon=True)

# Save figure (run from repo root: python3 codes/bm6.py)
os.makedirs('figs', exist_ok=True)
plt.savefig('figs/bm6.png', dpi=300)

# Open the image: termux-open on phone, normal window on laptop/PC
if shutil.which('termux-open'):
    subprocess.run(shlex.split("termux-open figs/bm6.png"))
else:
    plt.show()
