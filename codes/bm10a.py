import os
import shutil
import subprocess
import shlex

import numpy as np
import matplotlib.pyplot as plt

# Import custom matrix and vector modules
from CoordGeo.plotting.funcs import label_pts

# ---------------------------------------------------------
# Signal Parameters
# x(t) = 20*sin(100*pi*t) + 36*sin(150*pi*t) - 2*sin(300*pi*t)
# f1 = 50 Hz, f2 = 75 Hz, f3 = 150 Hz
# ---------------------------------------------------------
f1, A1 = 50, 20
f2, A2 = 75, 36
f3, A3 = 150, 2

f_max = 150      # Maximum frequency in Hz
duration = 4.0   # Time duration in seconds for fine FFT resolution


def spectrum(fs):
    """Return positive-frequency axis and amplitude spectrum for sampling rate fs."""
    t = np.arange(0, duration, 1 / fs)
    x = (
        A1 * np.sin(2 * np.pi * f1 * t)
        + A2 * np.sin(2 * np.pi * f2 * t)
        - A3 * np.sin(2 * np.pi * f3 * t)
    )
    N = len(t)
    X = np.fft.fft(x) / N
    freqs = np.fft.fftfreq(N, 1 / fs)
    mask = (freqs >= 0) & (freqs <= fs / 2)   # up to Nyquist limit
    return freqs[mask], 2 * np.abs(X[mask])


# Initialize figure
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 9), layout='constrained')

# =========================================================
# CASE 1: Non-Aliasing (fs = 500 Hz > 2 * f_max = 300 Hz)
# =========================================================
fs1 = 500   # Option (a)
freqs1, amp1 = spectrum(fs1)

ax1.stem(freqs1, amp1, linefmt='b-', markerfmt='bo', basefmt='k-')
ax1.set_title(r'Case 1: Non-Aliasing ($f_s = 500$ Hz $> 2f_{max}$)', fontsize=12)
ax1.set_xlabel('Frequency (Hz)')
ax1.set_ylabel('Amplitude')
ax1.set_xlim(0, 250)
ax1.set_ylim(0, 50)
ax1.grid(True, linestyle='--', alpha=0.5)

# Label the three peaks
peaks1 = np.array([[f1, f2, f3],
                   [A1, A2, A3]], dtype=float)
plt.sca(ax1)
label_pts(peaks1, ['50 Hz\n(Amp: 20)', '75 Hz\n(Amp: 36)', '150 Hz\n(Amp: 2)'])

# =========================================================
# CASE 2: Aliasing (fs = 200 Hz < 2 * f_max = 300 Hz)
# =========================================================
fs2 = 200   # Option (c)
freqs2, amp2 = spectrum(fs2)

ax2.stem(freqs2, amp2, linefmt='r-', markerfmt='ro', basefmt='k-')
ax2.set_title(r'Case 2: Aliasing ($f_s = 200$ Hz $< 2f_{max}$)', fontsize=12)
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Amplitude')
ax2.set_xlim(0, 110)
ax2.set_ylim(0, 50)
ax2.grid(True, linestyle='--', alpha=0.5)

# Label the peaks: 150 Hz folds onto 50 Hz, so 20 + 2 = 22
peaks2 = np.array([[f1, f2],
                   [A1 + A3, A2]], dtype=float)
plt.sca(ax2)
label_pts(peaks2, ['50 Hz (+ aliased 150 Hz)\n(Amp: 22)', '75 Hz\n(Amp: 36)'])

# Remove the outer plot box (spines)
for ax in (ax1, ax2):
    for spine in ax.spines.values():
        spine.set_visible(False)

# Save figure (run from repo root: python3 codes/bm10a.py)
os.makedirs('figs', exist_ok=True)
plt.savefig('figs/bm10a.png', dpi=300)

# Open the image: termux-open on phone, normal window on laptop/PC
if shutil.which('termux-open'):
    subprocess.run(shlex.split("termux-open figs/bm10a.png"))
else:
    plt.show()
