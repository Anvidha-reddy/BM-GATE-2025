#The implementation and plotting scripts are adapted from: 
#{https://github.com/Chamarthikrishnamadhur/ID1063/tree/master/07-09-26/BACTERIA}


import math
import matplotlib.pyplot as plt
import numpy as np
x1=np.linspace(0,0.2,20)
y1=3*np.exp(math.log(2)*x1)-2
x=np.loadtxt("x.dat") #taking input from dat file 
y=np.loadtxt("y.dat")
plt.plot(x1,y1,color='r')
plt.stem(x,y) #stem plot
plt.savefig("bac.png")
