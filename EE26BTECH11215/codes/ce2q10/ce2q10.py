# By Nehan mohammad
# 05-October-26, Monday, question no: village_triangle

import matplotlib.pyplot as plt
import numpy as np
import subprocess

# Triangle PQR with sides a=14 (QR), b=15 (RP), c=13 (PQ)
a, b, c = 14, 15, 13
s = (a + b + c) / 2
area = np.sqrt(s * (s - a) * (s - b) * (s - c))
h_a = (2 * area) / a

print(f"Area of Triangle: {area} sq km")
print(f"Minimum connecting road length (Altitude): {h_a} km")

# Generate and save triangle geometry figure
plt.figure(figsize=(7, 6))
plt.plot([0, 14, 5, 0], [0, 0, 12, 0], 'b-', linewidth=1.5)
plt.plot([5, 5], [0, 12], 'r--', linewidth=0.8, label=f'Altitude = {h_a:.1f} km')

plt.text(-0.8, -0.6, 'Q (0,0)', fontsize=9)
plt.text(13.5, -0.6, 'R (14,0)', fontsize=9)
plt.text(4.5, 12.4, 'P (5,12)', fontsize=9)

plt.xlim(-2, 16)
plt.ylim(-2, 14)

plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.legend(fontsize=9)
plt.title('Village Triangle PQR and Connecting Road', fontsize=10)
plt.xlabel('X Coordinate (km)', fontsize=9)
plt.ylabel('Y Coordinate (km)', fontsize=9)

plt.savefig('figs/village_triangle.png', dpi=300, bbox_inches='tight')

# subprocess.run(['termux-open', 'village_triangle.png'])
