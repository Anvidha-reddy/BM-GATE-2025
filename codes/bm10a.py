import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Signal Parameters
# x(t) = 20*sin(100*pi*t) + 36*sin(150*pi*t) - 2*sin(300*pi*t)
# f1 = 50 Hz, f2 = 75 Hz, f3 = 150 Hz
# ---------------------------------------------------------
f1, A1 = 50, 20
f2, A2 = 75, 36
f3, A3 = 150, 2

f_max = 150  # Maximum frequency in Hz
duration = 4.0  # Time duration in seconds for fine FFT resolution

# Create figure
plt.figure(figsize=(9, 9))

# =========================================================
# CASE 1: Non-Aliasing (fs = 500 Hz > 2 * f_max = 300 Hz)
# =========================================================
fs1 = 500  # Option (a)
t1 = np.arange(0, duration, 1 / fs1)
x1 = (
    A1 * np.sin(2 * np.pi * f1 * t1)
    + A2 * np.sin(2 * np.pi * f2 * t1)
    - A3 * np.sin(2 * np.pi * f3 * t1)
)

# Compute FFT & Magnitude Spectrum
N1 = len(t1)
X1 = np.fft.fft(x1) / N1
freqs1 = np.fft.fftfreq(N1, 1 / fs1)

# Extract positive frequencies up to Nyquist Limit (fs/2 = 250 Hz)
mask1 = (freqs1 >= 0) & (freqs1 <= fs1 / 2)
freqs1_pos = freqs1[mask1]
amp1 = 2 * np.abs(X1[mask1])

# Plot Case 1
plt.subplot(2, 1, 1)
plt.stem(freqs1_pos, amp1, linefmt="b-", markerfmt="bo", basefmt="k-")
plt.title("Case 1: Non-Aliasing ($f_s = 500$ Hz $> 2f_{max}$)", fontsize=12)
plt.xlabel("Frequency (Hz)", fontsize=11)
plt.ylabel("Amplitude", fontsize=11)
plt.xlim(0, 250)
plt.ylim(0, 45)
plt.grid(True, linestyle=":", alpha=0.7)

plt.text(
    50,
    22,
    "50 Hz\n(Amp: 20)",
    ha="center",
    va="bottom",
    fontweight="bold",
    color="blue",
)
plt.text(
    75,
    38,
    "75 Hz\n(Amp: 36)",
    ha="center",
    va="bottom",
    fontweight="bold",
    color="blue",
)
plt.text(
    150,
    4,
    "150 Hz\n(Amp: 2)",
    ha="center",
    va="bottom",
    fontweight="bold",
    color="blue",
)

# =========================================================
# CASE 2: Aliasing (fs = 200 Hz < 2 * f_max = 300 Hz)
# =========================================================
fs2 = 200  # Option (c)
t2 = np.arange(0, duration, 1 / fs2)
x2 = (
    A1 * np.sin(2 * np.pi * f1 * t2)
    + A2 * np.sin(2 * np.pi * f2 * t2)
    - A3 * np.sin(2 * np.pi * f3 * t2)
)

# Compute FFT & Magnitude Spectrum
N2 = len(t2)
X2 = np.fft.fft(x2) / N2
freqs2 = np.fft.fftfreq(N2, 1 / fs2)

# Extract positive frequencies up to Nyquist Limit (fs/2 = 100 Hz)
mask2 = (freqs2 >= 0) & (freqs2 <= fs2 / 2)
freqs2_pos = freqs2[mask2]
amp2 = 2 * np.abs(X2[mask2])

# Plot Case 2
plt.subplot(2, 1, 2)
plt.stem(freqs2_pos, amp2, linefmt="r-", markerfmt="ro", basefmt="k-")
plt.title("Case 2: Aliasing ($f_s = 200$ Hz $< 2f_{max}$)", fontsize=12)
plt.xlabel("Frequency (Hz)", fontsize=11)
plt.ylabel("Amplitude", fontsize=11)
plt.xlim(0, 110)
plt.ylim(0, 45)
plt.grid(True, linestyle=":", alpha=0.7)

plt.text(
    50,
    24,
    "50 Hz (Combines with aliased 150 Hz)\n(Amp: 22)",
    ha="center",
    va="bottom",
    fontweight="bold",
    color="red",
)
plt.text(
    75,
    38,
    "75 Hz\n(Amp: 36)",
    ha="center",
    va="bottom",
    fontweight="bold",
    color="red",
)

plt.tight_layout(pad=2.0)
plt.savefig("bm10a.png", dpi=300)
plt.close()
