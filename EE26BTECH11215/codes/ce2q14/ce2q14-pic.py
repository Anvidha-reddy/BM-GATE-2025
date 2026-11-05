import matplotlib.pyplot as plt
import subprocess

# Define node coordinates for the bridge truss
nodes = {
    'A': (0, 0), 'B': (6, 6), 'C': (6, 3), 'D': (6, 0),
    'E': (12, 6), 'F': (12, 3), 'G': (12, 0),
    'H': (18, 6), 'I': (18, 0),
    'J': (24, 6), 'K': (24, 3), 'L': (24, 0),
    'M': (30, 6), 'N': (30, 3), 'O': (30, 0),
    'P': (36, 0)
}

# Corrected structural members (edges) reflecting the proper Parker truss geometry
edges = [
    # Top chord
    ('B', 'E'), ('E', 'H'), ('H', 'J'), ('J', 'M'),
    # Bottom chord
    ('A', 'D'), ('D', 'G'), ('G', 'I'), ('I', 'L'), ('L', 'O'), ('O', 'P'),
    # Outer sloped end posts
    ('A', 'B'), ('M', 'P'),
    # Verticals
    ('B', 'C'), ('C', 'D'), ('E', 'F'), ('F', 'G'), ('H', 'I'), ('J', 'K'), ('K', 'L'), ('M', 'N'), ('N', 'O'),
    # Web diagonals (Left section)
    ('C', 'E'), ('C', 'G'),
    ('F', 'H'), ('F', 'I'),
    # Web diagonals (Right section - symmetric)
    ('K', 'H'), ('K', 'I'),
    ('N', 'J'), ('N', 'L')
]

plt.figure(figsize=(12, 4), dpi=300)

# Plot members with linewidth 0.5
for u, v in edges:
    p1, p2 = nodes[u], nodes[v]
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-', linewidth=0.5)

# Plot nodes and cleanly position labels
for name, pos in nodes.items():
    plt.plot(pos[0], pos[1], 'ko', markersize=3)
    y_offset = -0.6 if pos[1] == 0 else 0.4
    plt.text(pos[0], pos[1] + y_offset, name, fontsize=8, ha='center', va='center')

plt.grid(True, linestyle='--', alpha=0.5)
plt.axis('equal')
plt.xlim(-2, 38)
plt.ylim(-2, 9)
plt.title('Truss Structure - CE Q14', fontsize=10)
plt.xlabel('Length (m)', fontsize=9)
plt.ylabel('Height (m)', fontsize=9)

# Save figure and open with termux-open
plt.savefig('../../figs/ce2q14.png', dpi=300, bbox_inches='tight')
#subprocess.run(['termux-open', '../../figs/ce2q14.png'])
