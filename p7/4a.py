import numpy as np
import matplotlib.pyplot as plt

dt=0.001 # INPUT
tf=2.0
t0=0

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
l = np.radians(16) #angulo 

v0= 100/3.6  #vel inicial em min
t[0]=t0

v0x = v0*np.cos(l)
x0=-20   #posição inicial em x do ponto 3d (-10,y,z)
vx[0]= v0x
x[0]=x0

v0y = v0*np.sin(l)
y0=0  #posição inicial em y do ponto 3d (-10,1,z)
vy[0]= v0y
y[0]=y0


v0z = 0
z0=0 #posição inicial em z do ponto 3d (-10,1,0)
vz[0]= v0z
z[0]=z0

vt = 100/3.6 #vel terminal 
D = g/(vt**2)
v=np.empty(n+1)

for i in range(n): # Método de Euler
    v[i] = np.sqrt(vy[i]**2 + vx[i]**2 + vz[i]**2)
    ay[i] = -D*vy[i]*v[i] - g 
    ax[i] = -D*vx[i]*v[i]
    az[i] = 0 

    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt
    vz[i+1] = vz[i] + az[i]*dt

    y[i+1] = y[i] + vy[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    z[i+1] = z[i] + vz[i]*dt

#altura maxima ---> vy = 0
for i in range(n):
    if(x[i] < 0 and x[i+1] > 0):
        print(y[i+1])
        break
        

#plt.plot(x, y) 
#plt.xlabel("X (m)")
#plt.ylabel("Y (m)")
#plt.show()