#Calcule a altura máxima e o alcance (quando bate em y=0) da trajetória da bola de tenis 
#com rotação

import numpy as np
import matplotlib.pyplot as plt

dt=0.001 # INPUT
tf=2.0
t0=0

den = 1.225 #den ar
omega = 100 # w = (0,0,100) rad/s
massa = 0.057 #massa em g
raio = 0.067/2 
area = np.pi*raio**2
mag = 0.5*den*area*raio/massa

n=np.int((tf-t0)/dt)
t=t=np.linspace(t0, tf, n)

vy=np.empty(n+1)
y=np.empty(n+1)
ay=np.empty(n+1)

vx=np.empty(n+1)
x=np.empty(n+1)
ax=np.empty(n+1)

vz=np.empty(n+1)
z=np.empty(n+1)
az=np.empty(n+1)


g=9.80
l = np.radians(10) #angulo

v0= 130/3.6
t[0]=t0

v0y = v0*np.sin(l)
y0=1
vy[0]= v0y
y[0]=y0

v0x = v0*np.cos(l)
x0=-10
vx[0]= v0x
x[0]=x0

v0z = 0
z0=0
vz[0]= v0z
z[0]=z0

vt = 100/3.6
D = g/(vt**2)
v=np.empty(n+1)

for i in range(n): # Método de Euler
    
    amx = -mag*omega*vy[i]  #rotação
    amy = mag*omega*vx[i]  #rotação


    v[i] = np.sqrt(vy[i]**2 + vx[i]**2 + vz[i]**2)
    ay[i] = -D*vy[i]*v[i] - g  + amy
    ax[i] = -D*vx[i]*v[i] + amx
    az[i] = 0 

    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt
    vz[i+1] = vz[i] + az[i]*dt

    y[i+1] = y[i] + vy[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    z[i+1] = z[i] + vz[i]*dt

#altura maxima ---> vy = 0
for i in range(n):
    if (vy[i] > 0 and vy[i+1] < 0):
        print()
        print("Altura máxima  (t, y, v(m/s), v(km/h): ")
        print(t[i+1], y[i+1], vy[i+1], vy[i+1]*3600/1000)
        print()
        break

#regressa à posição inicial --> yo = 0
for i in range(n):
    if (y[i] > 0 and y[i+1] < 0):
        print()
        print("Alcance (t, x, v(m/s), v(km/h): ")
        print(t[i+1], x[i+1], vx[i+1], vx[i+1]*3600/1000)
        print()
        break



plt.plot(x, y) 
#plt.xlabel("X (m)")
#plt.ylabel("Y (m)")
plt.show()