from sympy import *
from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt



#b)

t0 = 0  #tempo inicial
x0 = 0 #posição inicial
v0x = 10 #velocidade inicial
dt = 0.1
tf=2
n=np.int((tf-t0)/dt+0.1)
t = np.linspace(0,n*dt,n+1) #matriz com os tempos
x = np.zeros(n+1)  
g = 9.8



ht = (v0x*t) - (g*(t**2))/2
print(ht)

vx = g*t #velocidade em cada t

t[0] = t0
x[0] = x0
vx[0] = v0x






for i in range(n):
    t[i+1]=t[i]+dt       #tempo
    x[i+1]=x[i]+vx[i]*dt #espaco




plt.plot(t,ht)

plt.show()



#c)


