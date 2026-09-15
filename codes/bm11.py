import matplotlib.pyplot as plt
import numpy as np

# 1. Define time vector (0 to 0.10 seconds)
t = np.linspace(0, 0.10, 1000)

# 2. Voltage V_s(t) in Volts and Current I(t) in mA
# V_s(t) = 5 * sin(100*t + pi/2)
# I(t) = 10 * sin(100*t + pi/6)
V_s = 5 * np.sin(100 * t + np.pi / 2)
I = 10 * np.sin(100 * t + np.pi / 6)

# 3. Compute Instantaneous Power p(t) in mW
p = V_s * I

# 4. Calculate Average Power P_avg (12.5 mW)
# P_avg = (V_m * I_m / 2) * cos(theta_v - theta_i) = 25 * cos(pi/3) = 12.5 mW
P_avg = 12.5

# 5. Create Plot
plt.figure(figsize=(9, 5))

# Plot Instantaneous Power curve
plt.plot(t, p, label="Instantaneous Power $p(t)$", color="tab:blue", linewidth=2)

# Plot Horizontal Line for Average Power
plt.axhline(
    y=P_avg,
    color="r",
    linestyle="--",
    linewidth=2,
    label=f"Average Power $P_{{avg}} = {P_avg}$ mW",
)

# Axis Labels and Styling
plt.xlabel("Time (s)", fontsize=12)
plt.ylabel("Power (mW)", fontsize=12)

plt.grid(True, linestyle=":", alpha=0.7)
plt.legend(fontsize=11, loc="upper right")

plt.tight_layout()

# Save plot to file
plt.savefig("bm11.png", dpi=300)
plt.close()
