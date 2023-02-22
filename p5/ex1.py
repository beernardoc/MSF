import math
import matplotlib.pyplot as plt


#a)
p = [3,4]

v = math.sqrt((p[0]**2)+(p[1]**2)) #comp ou norma do vetor 

#b)
puni = []
for x in p:
    puni.append((x/v))
    
v1 = math.sqrt((puni[0]**2)+(puni[1]**2)) #vetor unitario

#c)
p2 = []
for y in p:
    p2.append(2*y)

v2 = math.sqrt((p2[0]**2)+(p2[1]**2)) #vetor * 2









