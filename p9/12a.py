import math
from random import SystemRandom
import numpy as np
import matplotlib.pyplot as plt

dt=0.001 # INPUT
tf=100
t0=0
tolerancia = 0.000001


n=int((tf-t0)/dt)
t=np.linspace(t0, tf, n+1)
m = 75
u = 0.004
P = 0.4 * 735.4975
Cres = 0.9
A = 0.3
ro = 1.225
g = 9.80
vx=np.empty(n+1)
v=np.empty(n+1)
ax=np.empty(n+1)
x=np.empty(n+1)
v0 = 1
vx[0] = v0

for i in range(n): # Método de Euler
    v[i] = np.sqrt(vx[i]**2)
    ax[i] = -u*g - ((Cres)/(2*m))*A*ro*v[i]*vx[i] + (P/(m*v[i]))
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt

    if((vx[i] - vx[i-1]) < tolerancia): #quando a diferença de um ponto e seu antecessor for menos que 0.0001, este ja sera a vel terminal
        print(vx[i])
        break   






v[n] = np.sqrt(vx[n]**2)
ax[n] = -u*g - ((Cres/(2*m)))*A*ro*v[n]*vx[n] + (P/(m*v[n]))




plt.plot(t, v) 
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")
plt.show()


#fazer 12 b 