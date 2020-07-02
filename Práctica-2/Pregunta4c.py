import numpy as np
from scipy import interpolate

import matplotlib.pyplot as plt

# Puntos a usar
lista =np.array( [(-1,0), (1, 4), (3, -2), (4,3), (6,1)])
x=lista[:,0]
y=lista[:,1]


l=len(x)  

t=np.linspace(0,1,l-2,endpoint=True)
t=np.append([0,0,0],t)
t=np.append(t,[1,1,1])

tck=[t,[x,y],3]
u3=np.linspace(0,1,(max(l*2,70)),endpoint=True)
out = interpolate.splev(u3,tck)

plt.plot(x,y,'k--',label='Puntos de Control',marker='o',markerfacecolor='red')
plt.plot(out[0],out[1],'b',linewidth=2.0,label='B-Spline Curva')
plt.legend(loc='best')
plt.axis([min(x)-1, max(x)+1, min(y)-1, max(y)+1])
plt.title('Curva B-Spline Cúbica')
plt.show()

