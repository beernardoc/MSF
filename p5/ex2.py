import math

from numpy import mat

v1 = [1,2]
v2 = [-2,3]

cv1 = math.sqrt((v1[0]**2)+(v1[1]**2))
cv2 = math.sqrt((v2[0]**2)+(v2[1]**2))




pe = (v1[0]*v2[0]) + (v1[1]*v2[1])
print(pe)


cos = pe/((cv1)*(cv2))
angulo = math.degrees(math.acos(cos))
print(angulo)






