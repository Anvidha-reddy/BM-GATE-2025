import os
import shutil
import subprocess
import shlex

import numpy as np
import matplotlib.pyplot as plt

# Import custom matrix and vector modules
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

# Initialize figure with 2 vertical subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), layout='constrained')

# 1. Circuit parameters
R1 = 3000   # Ohms (3 kOhm)
R2 = 1000   # Ohms (1 kOhm)
C = 1e-6    # Farads (1 uF)

# 2. Frequency axis: omega from 1 to 5000 rad/s, generated as points on a line
A_w = np.array([1.0, 0.0]).reshape(-1, 1)
B_w = np.array([5000.0, 0.0]).reshape(-1, 1)
omega = line_gen_num(A_w, B_w, 1000)[0, :]

# 3. Input impedance Z_in(omega) = R1 + R2 / (1 + j*omega*R2*C)
Z_real = R1 + R2 / (1 + (omega * R2 * C) ** 2)
Z_imag = -(omega * (R2**2) * C) / (1 + (omega * R2 * C) ** 2)
Z_in = Z_real + 1j * Z_imag

# Magnitude (in kOhm) and phase (in degrees)
mag_Z = np.abs(Z_in) / 1000.0
phase_Z = np.angle(Z_in, deg=True)

# Values at omega = 1000 rad/s
w_op = 1000
idx_op = np.argmin(np.abs(omega - w_op))
P_mag = np.array([omega[idx_op], mag_Z[idx_op]]).reshape(-1, 1)
P_phase = np.array([omega[idx_op], phase_Z[idx_op]]).reshape(-1, 1)

# --- Subplot 1: Magnitude spectrum (top) ---
ax1.plot(omega, mag_Z, color='blue', linewidth=2.5,
         label=r'$|Z_{in}(\omega)| = \sqrt{Z_{real}^2 + Z_{imag}^2}$')
ax1.scatter(P_mag[0, 0], P_mag[1, 0], color='red', zorder=5, s=80)
plt.sca(ax1)
label_pts(P_mag, [rf'$\omega = 1000$ rad/s' + '\n' +
                  rf'$|Z_{{in}}| \approx {P_mag[1, 0]:.2f}$ k$\Omega$'])

ax1.set_title(r'Impedance Magnitude Spectrum $|Z_{in}(\omega)|$ vs $\omega$',
              fontsize=14, fontweight='bold')
ax1.set_xlabel(r'Angular Frequency $\omega$ (rad/s)')
ax1.set_ylabel(r'Magnitude $|Z_{in}|$ (k$\Omega$)')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0., frameon=True)

# --- Subplot 2: Phase spectrum (bottom) ---
ax2.plot(omega, phase_Z, color='purple', linewidth=2.5,
         label=r'$\angle Z_{in}(\omega) = \tan^{-1}\left(\frac{Z_{imag}}{Z_{real}}\right)$')
ax2.scatter(P_phase[0, 0], P_phase[1, 0], color='red', zorder=5, s=80)
plt.sca(ax2)
label_pts(P_phase, [rf'$\omega = 1000$ rad/s' + '\n' +
                    rf'$\angle Z_{{in}} \approx {P_phase[1, 0]:.2f}^\circ$'])

ax2.set_title(r'Impedance Phase Spectrum $\angle Z_{in}(\omega)$ vs $\omega$',
              fontsize=14, fontweight='bold')
ax2.set_xlabel(r'Angular Frequency $\omega$ (rad/s)')
ax2.set_ylabel(r'Phase $\angle Z_{in}$ (Degrees)')
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0., frameon=True)

# Remove the outer plot box (spines)
for ax in (ax1, ax2):
    for spine in ax.spines.values():
        spine.set_visible(False)

# Save figure (run from repo root: python3 codes/bm14.py)
os.makedirs('figs', exist_ok=True)
plt.savefig('figs/bm14.png', dpi=300)

# Open the image: termux-open on phone, normal window on laptop/PC
if shutil.which('termux-open'):
    subprocess.run(shlex.split("termux-open figs/bm14.png"))
else:
    plt.show()
