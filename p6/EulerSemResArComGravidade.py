import numpy as np
import matplotlib.pyplot as plt

dt=0.01 # INPUT
tf=1.0
t0=0

n=np.int((tf-t0)/dt)
t=t=np.linspace(t0, tf, n)

vy=np.empty(n+1)
y=np.empty(n+1)
ay=np.empty(n+1)

vx=np.empty(n+1)
x=np.empty(n+1)
ax=np.empty(n+1)


g=9.80
l = np.radians(10) #angulo

v0= (100*1000)/3600
t[0]=t0

v0y = v0*np.sin(l)
y0=0
vy[0]= v0y
y[0]=y0

v0x = v0*np.cos(l)
x0=0
vx[0]= v0x
x[0]=x0


for i in range(n): # Método de Euler
    ay[i] = -g
    ax[i] = 0

    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt

    y[i+1] = y[i] + vy[i]*dt
    x[i+1] = x[i] + vx[i]*dt

#está correto?
xanalitico = v0x*t + x0
yanalitico = v0y*t -(1/2)*g*(t**2) + y0
plt.plot(xanalitico, yanalitico, '-', label='Analítico sem resistência')
#------

plt.plot(x, y, '-', label='Euler sem resistencia')
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.show()