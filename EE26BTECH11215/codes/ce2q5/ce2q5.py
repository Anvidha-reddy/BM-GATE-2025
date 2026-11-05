import numpy as np
import matplotlib.pyplot as plt

# Equations:
# 2V + Y = 50
# V + G = 50
# Y + R = 50
# V + 2R = 50

A = np.array([
    [2, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 2, 0]
])
b = np.array([50, 50, 50, 50])

x = np.linalg.solve(A, b)
V, Y, R, G = x
total = np.sum(x)

print(f"V = {V:.0f}, Y = {Y:.0f}, R = {R:.0f}, G = {G:.0f}")

# Generate pie chart
labels = ['Violet (V)', 'Yellow (Y)', 'Red (R)', 'Green (G)']
sizes = [V, Y, R, G]
colors = ['purple', 'gold', 'indianred', 'forestgreen']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=140, colors=colors)
plt.title('Ball Distribution in the Bag')
plt.savefig('/home/nehan-mohammad/GATE-CE2-2025/figs/piechart.png', bbox_inches='tight')
plt.close()
