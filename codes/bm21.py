import os
import shutil
import subprocess
import shlex

import numpy as np
import matplotlib.pyplot as plt

# Import custom matrix and vector modules
from CoordGeo.plotting.funcs import label_pts

# Given values
R = 60
L = 0.01
C = 8e-6

# Resonance: net reactance is zero, so Z = R
w0 = 1 / np.sqrt(L * C)
print("Resonance frequency w0 =", w0, "rad/s")
print("I_rms at resonance =", 240 / R, "A")

# Positive and negative angular frequencies
w_pos = np.logspace(-5, 4, 5000)
w_neg = -w_pos[::-1]

# Impedance
Z_pos = R + 1j * (L * w_pos - 1 / (C * w_pos))
Z_neg = R + 1j * (L * w_neg - 1 / (C * w_neg))

# Magnitude and phase angle (degrees)
Zmag_pos = np.abs(Z_pos)
Zmag_neg = np.abs(Z_neg)
angle_pos = np.angle(Z_pos, deg=True)
angle_neg = np.angle(Z_neg, deg=True)

# Resonance points: |Z| = R and phase = 0
P_mag = np.array([w0, R]).reshape(-1, 1)
P_ang = np.array([w0, 0.0]).reshape(-1, 1)

# Initialize figure
fig, ax = plt.subplots(2, 1, figsize=(9, 10), layout='constrained')

# ---------------- MAGNITUDE ----------------
ax[0].plot(w_neg, Zmag_neg, 'b-')
ax[0].plot(w_pos, Zmag_pos, 'b-')
ax[0].scatter(P_mag[0, 0], P_mag[1, 0], color='red', zorder=5, s=60)
plt.sca(ax[0])
label_pts(P_mag, [r'Resonance: $\omega_0 \approx 3535.5$ rad/s, $|Z| = R = 60\ \Omega$'])

ax[0].set_xscale('symlog', linthresh=1)
ax[0].set_yscale('log')
ax[0].set_xlabel(r'Angular frequency $\omega$ (rad/s)')
ax[0].set_ylabel(r'$|Z(\omega)|$ ($\Omega$)')
ax[0].set_title(r'Impedance Magnitude $|Z(\omega)|$')
ax[0].grid(True, which='both', linestyle='--', alpha=0.3)

# ---------------- PHASE ANGLE ----------------
ax[1].plot(w_neg, angle_neg, 'b-')
ax[1].plot(w_pos, angle_pos, 'b-')
ax[1].scatter(P_ang[0, 0], P_ang[1, 0], color='red', zorder=5, s=60)
plt.sca(ax[1])
label_pts(P_ang, [r'Resonance: phase $= 0^\circ$'])

ax[1].set_xscale('symlog', linthresh=1)
ax[1].set_xlabel(r'Angular frequency $\omega$ (rad/s)')
ax[1].set_ylabel(r'Phase angle $\angle Z$ (degrees)')
ax[1].set_title(r'Impedance Phase Angle $\angle Z(\omega)$')
ax[1].grid(True, which='both', linestyle='--', alpha=0.3)

# Remove the outer plot box (spines)
for a in ax:
    for spine in a.spines.values():
        spine.set_visible(False)

# Save figure (run from repo root: python3 codes/bm21.py)
os.makedirs('figs', exist_ok=True)
plt.savefig('figs/bm21.png', dpi=300)

# Open the image: termux-open on phone, normal window on laptop/PC
if shutil.which('termux-open'):
    subprocess.run(shlex.split("termux-open figs/bm21.png"))
else:
    plt.show()
