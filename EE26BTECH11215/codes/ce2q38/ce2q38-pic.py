import matplotlib.pyplot as plt
import numpy as np
import subprocess

plt.figure(figsize=(10, 5), dpi=300)

# Left square element
sq_x = [-1, 1, 1, -1, -1]
sq_y = [-1, -1, 1, 1, -1]
plt.plot(sq_x, sq_y, 'k-', linewidth=0.5)

# Center axes for left square
plt.arrow(0, 0, 0, 1.2, head_width=0.08, head_length=0.12, fc='k', ec='k', linewidth=0.5)
plt.arrow(0, 0, 1.2, 0, head_width=0.08, head_length=0.12, fc='k', ec='k', linewidth=0.5)
plt.text(0.1, 1.3, 'y', fontsize=9)
plt.text(1.3, -0.2, 'x', fontsize=9)

# Stress arrows for left square
plt.arrow(-1, 0, -0.8, 0, head_width=0.08, head_length=0.12, fc='k', ec='k', linewidth=0.5)
plt.arrow(1, 0, 0.8, 0, head_width=0.08, head_length=0.12, fc='k', ec='k', linewidth=0.5)
plt.text(-1.5, 0.2, '$3\\sigma_0$', fontsize=9, ha='center')
plt.text(1.5, 0.2, '$3\\sigma_0$', fontsize=9, ha='center')

# Right square rotated by 45 degrees
theta = np.radians(45)
c, s = np.cos(theta), np.sin(theta)
R = np.array(((c, -s), (s, c)))
pts = np.array([[-1, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]])
rot_pts = np.dot(pts, R.T) + np.array([6, 0])
plt.plot(rot_pts[:, 0], rot_pts[:, 1], 'k-', linewidth=0.5)

# Center axes for right square
plt.arrow(6, 0, 0, 1.2, head_width=0.08, head_length=0.12, fc='k', ec='k', linewidth=0.5)
plt.arrow(6, 0, 1.2, 0, head_width=0.08, head_length=0.12, fc='k', ec='k', linewidth=0.5)
plt.text(6.1, 1.3, 'y', fontsize=9)
plt.text(7.3, -0.2, 'x', fontsize=9)

# Rotated stress arrow and angle arc
plt.arrow(6 - 1.414, 1.414, -0.6*c, -0.6*s, head_width=0.08, head_length=0.12, fc='k', ec='k', linewidth=0.5)
plt.text(4.2, 2.2, '$3\\sigma_0$', fontsize=9)

th = np.linspace(0, np.radians(45), 50)
plt.plot(6 - 1.414 + 0.4 * np.cos(th), 1.414 + 0.4 * np.sin(th), 'k-', linewidth=0.5)
plt.text(4.8, 1.1, '$45^\\circ$', fontsize=9)

plt.grid(True, linestyle='--', alpha=0.5)
plt.axis('equal')
plt.xlim(-3, 10)
plt.ylim(-2, 3)
plt.title('Stress Element Transformation - CE Q39', fontsize=10)

# Save figure and open with termux-open
plt.savefig('../../figs/ce2q39.png', dpi=300, bbox_inches='tight')
#subprocess.run(['termux-open', '../../figs/ce2q39.png'])
