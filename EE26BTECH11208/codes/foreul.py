import numpy as np
import math
import matplotlib.pyplot as plt
def eul(x,y):
    y=y+0.1*(3*y+2*math.exp(x))
    x=x+0.1
    return x,y
xth=np.linspace(0,3,3000)
yth=np.exp(3*xth)-np.exp(xth)
xeu=np.zeros(31)
yeu=np.zeros(31)
for i in range(30):
    xeu[i+1],yeu[i+1]=eul(xeu[i],yeu[i])
plt.title("Forward euler vs original")
plt.stem(xeu,yeu,label="forward euler")
plt.plot(xth,yth,color="red",label="original")
plt.xlim(0,2.5)
plt.ylim(0,900)
plt.legend()
plt.show()
