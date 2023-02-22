import numpy as np
import matplotlib.pyplot as plt

dt=0.001 # INPUT
tf=2.0
t0=0

n=np.int((tf-t0)/dt)
t=t=np.linspace(t0, tf, n+1)

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

em = np.empty(n+1)
m = 0.057




vt = 100/3.6
D = g/(vt**2)
v=np.empty(n+1)

for i in range(n): # Método de Euler
    v[i] = np.sqrt(vy[i]**2 + vx[i]**2)
    ay[i] = -D*vy[i]*v[i] - g #com a resitencia do ar
    ax[i] = -D*vx[i]*v[i] #com a resitencia do ar
   

    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt
   

    y[i+1] = y[i] + vy[i]*dt
    x[i+1] = x[i] + vx[i]*dt

    em[i] = 0.5*m*v[i]**2 + m*g*y[i] #energia mec

    if(i == 0):
        print("0.0")
        print(em[i])


    if(t[i] <= 0.4 < t[i+1]):
        print("0.4:")
        print(em[i])
    
    if(t[i] <= 0.8 < t[i+1]):
        print("0.8:")
        print(em[i])







v[n] = np.sqrt(vy[n]**2 + vx[n]**2) #para calcular o ultimo ponto
em[n] = 0.5*m*v[n]**2 + m*g*y[n] #para calcular o ultimo ponto




   
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


plt.plot(t, em) 
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.show()