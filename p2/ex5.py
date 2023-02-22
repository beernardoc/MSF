from re import M
from telnetlib import DM
from tkinter import Y
import numpy as np
import matplotlib.pyplot as plt


L=np.array([222.0,207.5,194,171.5,153.0,133.3,113.0,92.0])
X=np.array([2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0])

#Truque para não ter de alterar o código abaixo: identificar x e y corretamente
x = L
y = X


npontos=x.size

xy=x*y# element by element product
x2=x*x
y2=y*y

sx=x.sum()
sy=y.sum()
sxy=xy.sum()
sxx=x2.sum()
syy=y2.sum()

print("sx,sy,sxy,sxx,syy")
print(sx,sy,sxy,sxx,syy)

n=npontos
rn=n*sxy-sx*sy
rd=(n*sxx-sx**2)*(n*syy-sy**2)
r2=rn**2/rd
r=np.sqrt(r2)
m=(n*sxy-sx*sy)/(n*sxx-sx**2)
dm=abs(m)*np.sqrt((1/r**2-1)/(n-2))
bn=sxx*sy-sx*sxy  
bd=n*sxx-sx**2
b=bn/bd
db=dm*np.sqrt(sxx/n)





print('m +/-dm= ',m ,"+/-", dm)
print('b +/-db= ',b ,"+/-",db)
print('r2= ',r2)

#a:
plt.plot(x,y, "o")


#d
line_x = np.linspace(90,230,100)
line_y = m * line_x + b
plt.plot(line_x,line_y,"-r")


#e
novoL = float(input("digite o novo valor de L em cm" "\n"))
novoX = m * novoL + b
print('novo L:',novoL, "novo X:",novoX)


#f:
novoX1 = float(input("digite o novo valor de X em cm" "\n"))
novoL1 = (novoX1 - b)/m
print('novo X:',novoX1, "novo L:",novoL1)



plt.show()







