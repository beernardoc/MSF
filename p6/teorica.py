from turtle import color
import numpy as np
import matplotlib.pyplot as plt

# sai no teste

x0 = -20
y0 = 0
z0 = 0       

v0x = 25
v0y = 5
v0z = -50

wx = 0
wy = 400
wz = 0

t0 = 0
tfinal = 0.51
dt = 0.01
n=np.int64((tfinal-t0)/dt) #intervalo de tempo
t=np.linspace(t0,tfinal,n) #lista de intervalos de tempo

vy=np.zeros(n)
ay=np.zeros(n) 
y=np.zeros(n)
vx=np.zeros(n)
ax=np.zeros(n) 
x=np.zeros(n)
vz=np.zeros(n)
az=np.zeros(n) 
z=np.zeros(n)

vy[0]=v0y
y[0]=y0
vx[0]=v0x
x[0]=x0
vz[0]=v0z
z[0]=z0

massa = 0.45 # kg
raio_bola = 11 # cm
#area = pi * r2
densidade_ar = 1.225
vt = 100 / 3.6 #m/s
g = 9.8


for i in range(n - 1):
    t[i + 1] = t[i] + dt
    vv=np.sqrt(vx[i]**2+vy[i]**2+vz[i]**2)
    dres = g/vt**2
    mag=0.5*1.225*0.11*np.pi*0.11**2 #formula força magnus
    amx=(mag*wy*vz[i])/massa
    amz=(-mag*wy*vx[i])/massa
    ax[i]=-dres*vv*vx[i]+amx
    ay[i]=-g-dres*vv*vy[i]
    az[i]=-dres*vv*vz[i]+amz
    vx[i+1]=vx[i]+ax[i]*dt
    vy[i+1]=vy[i]+ay[i]*dt
    vz[i+1]=vz[i]+az[i]*dt
    x[i+1]=x[i]+vx[i]*dt
    y[i+1]=y[i]+vy[i]*dt
    z[i+1]=z[i]+vz[i]*dt

plt.plot(t, x, 'b-')
plt.plot(t, y, 'r-')
plt.plot(t, z, 'g-')
plt.grid()
plt.show()