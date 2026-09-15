import numpy as np
import matplotlib.pyplot as plt

# Time values
t = np.linspace(0, 0.1, 5000)

# Given signal
x = (20 * np.sin(100 * np.pi * t)
     + 36 * np.sin(150 * np.pi * t)
     - 2 * np.sin(300 * np.pi * t))

# Plot
plt.figure(figsize=(10, 5))
plt.plot(t, x)

plt.xlabel("t(seconds)")
plt.ylabel("x(t)")

plt.grid(True)

plt.tight_layout()
plt.savefig("bm10.png", dpi=150)
