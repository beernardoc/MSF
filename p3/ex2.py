from ast import Import

from tkinter.tix import Tree
from numpy import linspace, positive
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sp

vt = sp.Symbol('vt', real=True, positive=True)
g = sp.Symbol('g', real=True, positive=True)
t = sp.Symbol('t', real=True, positive=True)


vt = 6.8
g = 9.8

t = linspace(0,4,100)
print(t)

plt.plot(t, (vt**2)/g * np.log(np.cosh((g*t)/vt)))
plt.show()




