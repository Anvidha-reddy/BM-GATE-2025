import matplotlib.pyplot as plt
import numpy as np

# Time vector from t = 0 to 3 seconds
t = np.linspace(0, 3, 1000)

# Underdamped impulse response function c(t)
c_t = (10 / np.sqrt(3)) * np.exp(-2.5 * t) * np.sin((5 * np.sqrt(3) / 2) * t)

# Exponential decay envelope bounds
envelope = (10 / np.sqrt(3)) * np.exp(-2.5 * t)

# Plotting setup
plt.figure(figsize=(8, 5))
plt.plot(
    t,
    c_t,
    label=r"$c(t) = \frac{10}{\sqrt{3}} e^{-\frac{5}{2}t} \sin\left(\frac{5\sqrt{3}}{2}t\right)$",
    color="blue",
    linewidth=2,
)
plt.plot(t, envelope, "--", color="red", alpha=0.5, label="Decay Envelope")
plt.plot(t, -envelope, "--", color="red", alpha=0.5)

# Formatting
plt.title("Underdamped Impulse Response $c(t)$", fontsize=14)
plt.xlabel("time (s)", fontsize=12)
plt.ylabel("c(t)", fontsize=12)
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper right", fontsize=10)
plt.tight_layout()

# Save plot as bm6.png
plt.savefig("bm6.png", dpi=300)
plt.close()
