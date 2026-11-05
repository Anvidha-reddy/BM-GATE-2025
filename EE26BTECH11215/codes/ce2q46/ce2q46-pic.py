import matplotlib.pyplot as plt
import subprocess

# Define node coordinates with balanced proportional geometry
nodes = {
    'A': (-6, 3.0),
    'B': (-4, 3.5),  # Lies perfectly on the straight line from A(-6,3) to F(0,4.5)
    'C': (-4, 3.0),
    'D': (-2, 4.0),  # Lies perfectly on the straight line from A(-6,3) to F(0,4.5)
    'E': (-2, 3.0),
    'F': (0, 4.5),   # Reduced height for better proportion
    'G': (0, 3.0),
    'H': (2, 4.5),   # Reduced height matching F
    'I': (2, 3.0),
    'J': (0, 1.5),
    'K': (2, 1.5),
    'L': (0, 0),
    'M': (2, 0)
}

# Structural members (edges)
edges = [
    # Top chord
    ('A', 'B'), ('B', 'D'), ('D', 'F'), ('F', 'H'),
    # Bottom chord and extensions
    ('A', 'C'), ('C', 'E'), ('E', 'G'), ('G', 'I'),
    # Verticals
    ('B', 'C'), ('D', 'E'), ('F', 'G'), ('H', 'I'),
    ('G', 'J'), ('I', 'K'), ('J', 'L'), ('K', 'M'),
    # Tower horizontals
    ('J', 'K'), ('L', 'M'),
    # Web diagonals (cantilever section)
    ('B', 'E'), ('F', 'E'),
    # Tower diagonals
    ('F', 'I'), ('J', 'I'), ('J', 'M')
]

plt.figure(figsize=(10, 7), dpi=300)
ax = plt.gca()

# Plot structural members with clean engineering linewidth
for u, v in edges:
    p1, p2 = nodes[u], nodes[v]
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-', linewidth=0.8, zorder=2)

# Plot nodes as solid black dots
for pos in nodes.values():
    plt.plot(pos[0], pos[1], 'ko', markersize=3.5, zorder=3)

# Position node labels to match layout cleanly
label_offsets = {
    'A': (-0.3, 0),
    'B': (-0.3, 0.2),
    'C': (0, -0.3),
    'D': (0.3, 0.2),
    'E': (0.3, -0.3),
    'F': (-0.3, 0.25),
    'G': (0.3, 0),
    'H': (0.3, 0.25),
    'I': (0.3, 0),
    'J': (-0.3, 0),
    'K': (0.3, 0),
    'L': (-0.3, -0.3),
    'M': (0.3, -0.3)
}

for name, pos in nodes.items():
    dx, dy = label_offsets.get(name, (0.2, 0.2))
    ha = 'right' if dx < 0 else ('left' if dx > 0 else 'center')
    va = 'top' if dy < 0 else ('bottom' if dy > 0 else 'center')
    plt.text(pos[0] + dx, pos[1] + dy, name, fontsize=10, ha=ha, va=va, zorder=4)

# 60 kN downward load vector at node B (-4, 3.5)
plt.arrow(-4, 4.5, 0, -0.8, head_width=0.15, head_length=0.22, fc='k', ec='k', linewidth=0.8, zorder=5)
plt.text(-4, 4.7, '60 kN', fontsize=10, ha='center', va='bottom', zorder=5)

# Enforce clean layout, equal aspect ratio, and remove axes
ax.set_aspect('equal')
plt.axis('off')
plt.xlim(-7.2, 3.2)
plt.ylim(-0.5, 5.2)

# Save figure and open via termux-open
plt.savefig('../../figs/ce2q46.png', dpi=300, bbox_inches='tight', transparent=False)
#subprocess.run(['termux-open', '../../figs/ce2q46.png'])
