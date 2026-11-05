# By Nehan mohammad
# 05-October-26, Monday, question no: influence_line_gi

import matplotlib.pyplot as plt
import numpy as np
import subprocess

x = np.array([0, 6, 12, 18, 24, 30, 36])
y = np.array([0, 0.33, 1.33, 1.00, 0.67, 0.33, 0])

plt.figure(figsize=(9, 4))
plt.plot(x, y, marker='o', color='red', linewidth=0.5, markersize=4)

joints = ['A', 'D', 'G', 'I', 'L', 'O', 'P']
for xi, yi, joint in zip(x, y, joints):
    plt.text(xi, yi + 0.08, f'{joint}\n({yi:.2f})' if yi > 0 else f'{joint}\n(0)', 
             ha='center', va='bottom', fontsize=8)

plt.title('Influence Line Diagram for Member G-I', fontsize=10)
plt.xlabel('Position of Unit Load Along Bottom Chord (m)', fontsize=9)
plt.ylabel('Influence Ordinate (Force)', fontsize=9)
plt.xticks(x, [f'{j}\n({pos}m)' for j, pos in zip(joints, x)], fontsize=8)
plt.ylim(-0.1, 1.6)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
plt.axhline(0, color='black', linewidth=0.8)

plt.savefig('figs/influence_line_gi.png', dpi=300, bbox_inches='tight')

# subprocess.run(['termux-open', 'influence_line_gi.png'])
