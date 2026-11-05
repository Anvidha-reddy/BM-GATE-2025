# By Nehan mohammad
# 05-October-26, Monday, question no: cantilever_deflection

import matplotlib.pyplot as plt
import numpy as np
import subprocess

L = 10.0
M = 50.0
Delta = 0.01
EI = 10000.0

R_b = (3 * M / (2 * L)) - (3 * EI * Delta / (L**3))
print(f"Upward Reaction at B = {R_b:.2f} N")

x = np.linspace(0, L, 100)
deflection = -(M * x**2) / (2 * EI) + (R_b * x**3) / (6 * EI)

plt.figure(figsize=(8, 5))
plt.plot(x, deflection, color='purple', linewidth=0.8, label='Deflection Curve')
plt.grid(True)
plt.title('Propped Cantilever Deflection Curve')
plt.xlabel('Length (m)')
plt.ylabel('Deflection (m)')
plt.legend()
plt.savefig('figs/cantilever_deflection.png', dpi=300, bbox_inches='tight')

# subprocess.run(['termux-open', 'cantilever_deflection.png'])
