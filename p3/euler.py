from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt




t0 = 0  #tempo inicial
x0 = 800
v0x = -60 #velocidade inicial
dt = 0.25
tf=100
n=np.int((tf-t0)/dt+0.1)
t = linspace(0,n*dt,n+1) #matriz com os tempos
x = np.zeros(n+1)  
g = 9.8
vx = g*t #velocidade em cada t

t[0] = t0
x[0] = x0
vx[0] = v0x
print(n)

for i in range(n):
    t[i+1]=t[i]+dt
    x[i+1]=x[i]+vx[i]*dt








plt.plot(t,x)

plt.show()



