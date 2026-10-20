import os
import shutil
import subprocess
import shlex
from fractions import Fraction

import numpy as np
import matplotlib.pyplot as plt

# Import custom matrix and vector modules
from CoordGeo.plotting.funcs import label_pts

# Range of n
n = np.arange(-5, 11)


# Unit impulse function
def delta(n):
    return (n == 0).astype(int)


# x[n] = delta[n] + delta[n-1]
x = delta(n) + delta(n - 1)

# h[n] = delta[n] + (1/2)delta[n-1] + (1/3)delta[n-2]
h = delta(n) + (1 / 2) * delta(n - 1) + (1 / 3) * delta(n - 2)

# y[n] = x[n] * h[n] (linear convolution)
# The full convolution starts at n = 2*n[0], so slice it back onto the same n axis
full = np.convolve(x, h)
y = full[-n[0]: -n[0] + len(n)]

print("y[n] for n = 0..3:", y[n >= 0][:4])


def frac(v):
    return str(Fraction(float(v)).limit_denominator(100))


# Initialize figure
fig, axes = plt.subplots(3, 1, figsize=(8, 8), layout='constrained')

signals = [
    (x, 'x[n]', 'Input Signal x[n]'),
    (h, 'h[n]', 'Impulse Response h[n]'),
    (y, 'y[n]', 'Output Signal y[n]'),
]

for ax, (sig, ylab, title) in zip(axes, signals):
    ax.stem(n, sig, basefmt='k-')
    ax.set_title(title)
    ax.set_xlabel('n')
    ax.set_ylabel(ylab)
    ax.set_ylim(0, 1.3 * np.max(sig))
    ax.set_xticks(n)
    ax.grid(True, linestyle='--', alpha=0.5)

    # Label the nonzero samples with their values
    idx = np.nonzero(np.abs(sig) > 1e-12)[0]
    pts = np.array([n[idx], sig[idx]], dtype=float)
    plt.sca(ax)
    label_pts(pts, [frac(v) for v in sig[idx]])

    # Remove the outer plot box (spines)
    for spine in ax.spines.values():
        spine.set_visible(False)

# Save figure (run from repo root: python3 codes/bm17a.py)
os.makedirs('figs', exist_ok=True)
plt.savefig('figs/bm17a.png', dpi=300)

# Open the image: termux-open on phone, normal window on laptop/PC
if shutil.which('termux-open'):
    subprocess.run(shlex.split("termux-open figs/bm17a.png"))
else:
    plt.show()
