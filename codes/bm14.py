import matplotlib.pyplot as plt
import numpy as np

# 1. Circuit Parameters
R1 = 3000  # Ohms (3 kOmega)
R2 = 1000  # Ohms (1 kOmega)
C = 1e-6  # Farads (1 uF)

# Frequency range: omega from 0 to 5000 rad/s
omega = np.linspace(1, 5000, 1000)

# 2. Symbolic/Analytical Impedance Calculation
# Real and Imaginary components of Z_in(omega)
Z_real = R1 + R2 / (1 + (omega * R2 * C) ** 2)
Z_imag = -(omega * (R2**2) * C) / (1 + (omega * R2 * C) ** 2)

# Complex input impedance
Z_in = Z_real + 1j * Z_imag

# Magnitude (in kOhms) and Phase (in Degrees)
mag_Z = np.abs(Z_in) / 1000.0  # kOmega
phase_Z = np.angle(Z_in, deg=True)  # Degrees

# Calculate values specifically at omega = 1000 rad/s
w_op = 1000
idx_op = np.argmin(np.abs(omega - w_op))
mag_op = mag_Z[idx_op]
phase_op = phase_Z[idx_op]

# 3. Create Large Stacked Figure (2x1 Grid)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# --- Subplot 1: Magnitude Spectrum (Top Plot) ---
ax1.plot(
    omega,
    mag_Z,
    color="blue",
    linewidth=2.5,
    label=r"$|Z_{in}(\omega)| = \sqrt{Z_{real}^2 + Z_{imag}^2}$",
)
ax1.scatter([w_op], [mag_op], color="red", zorder=5, s=80)
ax1.annotate(
    f"At $\\omega = 1000$ rad/s\n$|Z_{{in}}| \\approx {mag_op:.2f}$ k$\\Omega$",
    (w_op, mag_op),
    textcoords="offset points",
    xytext=(35, 15),
    fontsize=11,
    fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="red", lw=1.5),
)

ax1.set_title(
    r"Impedance Magnitude Spectrum $|Z_{in}(\omega)|$ vs $\omega$",
    fontsize=14,
    fontweight="bold",
    pad=10,
)
ax1.set_xlabel(r"Angular Frequency $\omega$ (rad/s)", fontsize=12)
ax1.set_ylabel(r"Magnitude $|Z_{in}|$ (k$\Omega$)", fontsize=12)
ax1.grid(True, linestyle=":", alpha=0.6)
ax1.legend(fontsize=11)

# --- Subplot 2: Phase Spectrum (Bottom Plot) ---
ax2.plot(
    omega,
    phase_Z,
    color="purple",
    linewidth=2.5,
    label=r"$\angle Z_{in}(\omega) = \tan^{-1}\left(\frac{Z_{imag}}{Z_{real}}\right)$",
)
ax2.scatter([w_op], [phase_op], color="red", zorder=5, s=80)
ax2.annotate(
    f"At $\\omega = 1000$ rad/s\n$\\angle Z_{{in}} \\approx {phase_op:.2f}^\\circ$",
    (w_op, phase_op),
    textcoords="offset points",
    xytext=(35, -25),
    fontsize=11,
    fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="red", lw=1.5),
)

ax2.set_title(
    r"Impedance Phase Spectrum $\angle Z_{in}(\omega)$ vs $\omega$",
    fontsize=14,
    fontweight="bold",
    pad=10,
)
ax2.set_xlabel(r"Angular Frequency $\omega$ (rad/s)", fontsize=12)
ax2.set_ylabel(r"Phase $\angle Z_{in}$ (Degrees)", fontsize=12)
ax2.grid(True, linestyle=":", alpha=0.6)
ax2.legend(fontsize=11)

plt.tight_layout(pad=2.5)
plt.savefig("bm14.png", dpi=300)
plt.close()
