from re import T
from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt
import math


#a)




ap = 9.8  #aceleração patrulha
va = 60  #vel de a em ms
n = 100  #passo
tempo = np.linspace(0,20,n)  #matriz com os tempos de 0 a 20 no passo n

xa = va * tempo  #distancia percorrida por a no tempo
xp = 0.5*ap*tempo**2  #distancia percorrida por p no tempo




#b)
te = (2*va)/ap #tempo encontro
xe = va * te #distancia encontro


plt.plot(te,xe, "o")

plt.show()








