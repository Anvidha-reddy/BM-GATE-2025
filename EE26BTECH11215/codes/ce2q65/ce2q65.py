import numpy as np
import matplotlib.pyplot as plt

# Inputs directly from the problem statement
fb_ab = 60.0  # Fore bearing of AB
fb_bc = 122.0 # Fore bearing of BC

# Basic vector setup for plotting lines meeting at B (0, 0)
bb_ba = fb_ab + 180.0  # Back bearing calculation
Bx, By = 0, 0
length = 5

# Convert bearings to standard math angles
angle_ba = np.radians(90 - bb_ba)
angle_bc = np.radians(90 - fb_bc)

Ax = Bx + length * np.cos(angle_ba)
Ay = By + length * np.sin(angle_ba)
Cx = Bx + length * np.cos(angle_bc)
Cy = By + length * np.sin(angle_bc)

# Plotting
plt.figure(figsize=(6, 6))
plt.plot([Ax, Bx], [Ay, By], 'b-', linewidth=2, label='Line BA')
plt.plot([Bx, Cx], [By, Cy], 'r-', linewidth=2, label='Line BC')
plt.scatter([Ax, Bx, Cx], [Ay, By, Cy], color=['blue', 'black', 'red'])

plt.axhline(0, color='gray', linestyle='--', alpha=0.5)
plt.axvline(0, color='gray', linestyle='--', alpha=0.5)
plt.title('Lines BA and BC Meeting at Point B', fontsize=12)
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.grid(True)
plt.legend(loc='upper right')
plt.gca().set_aspect('equal', adjustable='box')

# Save the figure instead of showing it interactively
plt.savefig('/home/nehan-mohammad/GATE-CE2-2025/figs/interior_angle.png', dpi=300, bbox_inches='tight')

plt.close()
