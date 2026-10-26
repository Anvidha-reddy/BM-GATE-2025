import os
import shutil
import subprocess
import shlex

import numpy as np
import matplotlib.pyplot as plt

# Import custom matrix and vector modules
from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

# Given values
R = 60
L = 0.01
C = 8e-6

# Resonance: net reactance is zero, so Z = R
w0 = 1 / np.sqrt(L * C)
f0 = w0 / (2 * np.pi)
print("Resonance frequency w0 =", w0, "rad/s")
print("Resonance frequency f0 =", f0, "Hz")
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
label_pts(P_mag, [rf'Resonance: $|Z| = R = {R}\ \Omega$' + '\n' + rf'$\omega_0 \approx {w0:.1f}$ rad/s ($f_0 \approx {f0:.1f}$ Hz)'])

ax[0].set_xscale('symlog', linthresh=1)
ax[0].set_yscale('log')
ax[0].set_xlabel(r'Angular frequency $\omega$ (rad/s)')
ax[0].set_ylabel(r'$|Z(\omega)|$ ($\Omega$)')
ax[0].set_title(r'Impedance Magnitude $|Z(\omega)|$')
ax[0].grid(True, which='both', linestyle='--', alpha=0.3)

# Mark resonance frequency and amplitude with guide lines to the axes
ax[0].set_ylim(bottom=5)
xlim = ax[0].get_xlim()
ylim = ax[0].get_ylim()
x_v = line_gen_num(np.array([w0, ylim[0]]).reshape(-1, 1), P_mag, 50)
x_h = line_gen_num(np.array([xlim[0], R]).reshape(-1, 1), P_mag, 50)
ax[0].plot(x_v[0, :], x_v[1, :], 'r--', linewidth=1)
ax[0].plot(x_h[0, :], x_h[1, :], 'r--', linewidth=1)
ax[0].annotate(rf'$\omega_0 = {w0:.1f}$', (w0, ylim[0]), textcoords='offset points',
               xytext=(0, 8), ha='center', color='red')
ax[0].annotate(rf'$|Z| = {R}\ \Omega$', (xlim[0], R), textcoords='offset points',
               xytext=(5, 6), ha='left', color='red')
ax[0].set_xlim(xlim)
ax[0].set_ylim(ylim)

# ---------------- PHASE ANGLE ----------------
ax[1].plot(w_neg, angle_neg, 'b-')
ax[1].plot(w_pos, angle_pos, 'b-')
ax[1].scatter(P_ang[0, 0], P_ang[1, 0], color='red', zorder=5, s=60)
plt.sca(ax[1])
label_pts(P_ang, [rf'Resonance: phase $= 0^\circ$' + '\n' + rf'$\omega_0 \approx {w0:.1f}$ rad/s ($f_0 \approx {f0:.1f}$ Hz)'])

ax[1].set_xscale('symlog', linthresh=1)
ax[1].set_xlabel(r'Angular frequency $\omega$ (rad/s)')
ax[1].set_ylabel(r'Phase angle $\angle Z$ (degrees)')
ax[1].set_title(r'Impedance Phase Angle $\angle Z(\omega)$')
ax[1].grid(True, which='both', linestyle='--', alpha=0.3)

# Mark resonance frequency with a guide line to the axis
xlim = ax[1].get_xlim()
ylim = ax[1].get_ylim()
x_v = line_gen_num(np.array([w0, ylim[0]]).reshape(-1, 1), P_ang, 50)
ax[1].plot(x_v[0, :], x_v[1, :], 'r--', linewidth=1)
ax[1].annotate(rf'$\omega_0 = {w0:.1f}$', (w0, ylim[0]), textcoords='offset points',
               xytext=(0, 8), ha='center', color='red')
ax[1].set_xlim(xlim)
ax[1].set_ylim(ylim)

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
