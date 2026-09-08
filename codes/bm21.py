import numpy as np
import matplotlib.pyplot as plt

# Given values
R = 60
L = 0.01
C = 8e-6

# Positive and negative angular frequencies
w_pos = np.logspace(-5, 4, 5000)
w_neg = -w_pos[::-1]

# Impedance
Z_pos = R + 1j * (L*w_pos - 1/(C*w_pos))
Z_neg = R + 1j * (L*w_neg - 1/(C*w_neg))

# Magnitude
Zmag_pos = np.abs(Z_pos)
Zmag_neg = np.abs(Z_neg)

# Phase angle in degrees
angle_pos = np.angle(Z_pos, deg=True)
angle_neg = np.angle(Z_neg, deg=True)

# Create subplots
fig, ax = plt.subplots(2, 1, figsize=(9, 10))

# ---------------- MAGNITUDE ----------------
ax[0].plot(w_neg, Zmag_neg)
ax[0].plot(w_pos, Zmag_pos)

ax[0].set_xscale('symlog', linthresh=1)
ax[0].set_yscale('log')

ax[0].set_xlabel(r'Angular frequency $\omega$ (rad/s)')
ax[0].set_ylabel(r'$|Z(\omega)|$ ($\Omega$)')
ax[0].set_title(r'Impedance Magnitude $|Z(\omega)|$')
ax[0].grid(True, which='both', alpha=0.3)

# ---------------- PHASE ANGLE ----------------
ax[1].plot(w_neg, angle_neg)
ax[1].plot(w_pos, angle_pos)

ax[1].set_xscale('symlog', linthresh=1)

ax[1].set_xlabel(r'Angular frequency $\omega$ (rad/s)')
ax[1].set_ylabel(r'Phase angle $\angle Z$ (degrees)')
ax[1].set_title(r'Impedance Phase Angle $\angle Z(\omega)$')
ax[1].grid(True, which='both', alpha=0.3)

plt.tight_layout()

# Save the graph
plt.savefig('impedance_magnitude_phase.png', dpi=300)
