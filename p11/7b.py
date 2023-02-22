import numpy as np
import matplotlib.pyplot as plt

dt=0.01 # INPUT
tf=200
t0=0

n=np.int((tf-t0)/dt)
t=t=np.linspace(t0, tf, n+1)




vx=np.empty(n+1)
x=np.empty(n+1)
ax=np.empty(n+1)


g=9.80


v0= 0
t[0]=t0


v0x = 0 #questao
x0= 4 #questao
vx[0]= v0x
x[0]=x0


k = 1 #questao
m = 1 #questao
omega = 1 # np.sqrt(k/m) nesse caso é 1

arrayx = []
tempos = []
periodos = []

for i in range(n): # Método de Euler cromer
    
    ax[i] = (-k/m)*x[i]

    
    vx[i+1] = vx[i] + ax[i]*dt

   
    x[i+1] = x[i] + vx[i+1]*dt

    if(x[i-1] < x[i] > x[i+1] and i> 0):
        arrayx.append(x[i])
        tempos.append(t[i])

for i in range(len(tempos)-1):
    periodos.append(tempos[i+1] - tempos[i])


        

amplitude = sum(arrayx)/len(arrayx)
print(amplitude)



periodos = sum(periodos)/len(periodos);
print(periodos)


    

plt.plot(t,x,)

plt.show()