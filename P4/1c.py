from sympy import *
from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt


t0 = 0  #tempo inicial
x0 =  800 #posição inicial
v0x = 0 #velocidade inicial
dt = 0.025
tf=4.0
n=np.int((tf-t0)/dt+0.1)
t = np.linspace(0,n*dt,n+1) #matriz com os tempos
x = np.zeros(n+1)  
g = 9.8



vx = g*t #velocidade em cada t

t[0] = t0
x[0] = x0
vx[0] = v0x






for i in range(n):
    t[i+1]=t[i]+dt       #tempo
    x[i+1]=x[i]+vx[i]*dt #espaco



pontot = t[int((3/dt))]  #tempo 3 segundos no vetor dos tempos (posição 120) 
pontox = vx[int((3/dt))] #tempo 3 segundos no vetor da vel (posição 120)

print(pontot,pontox)


plt.plot(t,vx)
plt.plot(pontot,pontox, "o")
plt.show()