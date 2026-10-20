#The code has been adapted from {https://github.com/gadepall/matgeo/tree/main/codes/CoordGeo}
#Must be run inside matgeo/codes/CoordGeo/ 
import sys
sys.path.insert(0, '/sdcard/github/matgeo/codes/CoordGeo')
import numpy as np
import matplotlib.pyplot as plt

from line.funcs import * #takes import form line/funcs.py
from conics.funcs import circ_gen #takes imports from conics/funcs.py

import subprocess
import shlex #for running and opening in termux

# defining origin vectors
O1 = np.array([0.5, 0]).reshape(-1, 1)
r1 = 0.5 

O2 = np.array([1, 1]).reshape(-1, 1)
r2 = 1

#taking vector arrays
X1 = np.array([0.2, 0.4]).reshape(-1, 1)
X2 = np.array([1, 0]).reshape(-1, 1) 

#implementing required circles 
x_circ1 = circ_gen(O1, r1)
x_circ2 = circ_gen(O2, r2) 

P1 = X1 + 0.5 * (X1 - X2)
P2 = X2 + 0.5 * (X2 - X1)
x_rad = line_gen(P1, P2)

x_centers = line_gen(O1, O2) #to get the line of intersection of origins

#Plotting: 
plt.figure(figsize=(8, 8))

plt.plot(x_circ1[0,:], x_circ1[1,:], color='blue', label='$Circle\\ 1$')
plt.plot(x_circ2[0,:], x_circ2[1,:], color='orange', label='$Circle\\ 2$')
plt.plot(x_rad[0,:], x_rad[1,:], color='green', linestyle='--', label='$Radical\\ Axis$')
plt.plot(x_centers[0,:], x_centers[1,:], color='black', linestyle='-.', label='$Line\\ of\\ Centers$')

coords = np.block([[O1, O2, X1, X2]])
plt.scatter(coords[0,:], coords[1,:], color='red', zorder=5)

vert_labels = ['o_1(0.5, 0)', 'o_2(1, 1)', 'x_1(0.2, 0.4)', 'x_2(1, 0)']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'${txt}$',      #annotates req coordinates
                 (coords[0,i], coords[1,i]), 
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center',
                 fontsize=12)

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper left')
plt.grid(True, linestyle=':')
plt.axis('equal')

plt.savefig('figs/conics/circleintersect.pdf')
#for opening in termux automatically: 
#subprocess.run(shlex.split("termux-open figs/conics/circle_intersect.pdf")) 

