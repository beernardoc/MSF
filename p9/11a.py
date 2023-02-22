import numpy as np
import matplotlib.pyplot as plt

v = 30/3.6
m = 75
u = 0.004
Cres = 0.9
A = 0.3
ro = 1.225
g = 9.80
vx = v

P = u*m*g*v + (Cres/2)*A*ro*(v**2)*vx 
print(P)