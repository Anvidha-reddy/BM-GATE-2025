import os
import shutil
import subprocess
import shlex

import numpy as np
import matplotlib.pyplot as plt

# Import custom matrix and vector modules
from CoordGeo.line.funcs import line_gen, line_gen_num

# Initialize figure
fig, ax = plt.subplots(figsize=(9, 5), layout='constrained')

# 1. Time axis (0 to 0.10 s) generated as points on a line
A_ax = np.array([0.0, 0.0]).reshape(-1, 1)
B_ax = np.array([0.10, 0.0]).reshape(-1, 1)
x_ax = line_gen_num(A_ax, B_ax, 1000)
t = x_ax[0, :]

# 2. Voltage V_s(t) in Volts and current I(t) in mA
#    V_s(t) = 5 sin(100 t + pi/2),  I(t) = 10 sin(100 t + pi/6)
Vm, Im = 5.0, 10.0
phi_v, phi_i = np.pi / 2, np.pi / 6
V_s = Vm * np.sin(100 * t + phi_v)
I = Im * np.sin(100 * t + phi_i)

# 3. Instantaneous power p(t) in mW
p = V_s * I

# 4. Average power: P_avg = (Vm*Im/2) cos(phi_v - phi_i) = 12.5 mW
P_avg = 0.5 * Vm * Im * np.cos(phi_v - phi_i)

# 5. Horizontal line at P_avg using line points
A_avg = np.array([0.0, P_avg]).reshape(-1, 1)
B_avg = np.array([0.10, P_avg]).reshape(-1, 1)
x_avg = line_gen(A_avg, B_avg)

# Plot
ax.plot(t, p, color='tab:blue', linewidth=2, label=r'Instantaneous Power $p(t)$')
ax.plot(x_avg[0, :], x_avg[1, :], 'r--', linewidth=2,
        label=rf'Average Power $P_{{avg}} = {P_avg:.1f}$ mW')

# Formatting plot area
ax.set_xlim(0, 0.10)
ax.grid(True, linestyle='--', alpha=0.5)

# Remove the outer plot box (spines)
for spine in ax.spines.values():
    spine.set_visible(False)

# Axis labels
ax.set_xlabel('Time (s)')
ax.set_ylabel('Power (mW)')

# Legend
ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0., frameon=True)

# Save figure (run from repo root: python3 codes/bm11.py)
os.makedirs('figs', exist_ok=True)
plt.savefig('figs/bm11.png', dpi=300)

# Open the image: termux-open on phone, normal window on laptop/PC
if shutil.which('termux-open'):
    subprocess.run(shlex.split("termux-open figs/bm11.png"))
else:
    plt.show()
