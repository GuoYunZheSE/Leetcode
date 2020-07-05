# @Date    : 21:19 07/02/2020
# @Author  : ClassicalPi
# @FileName: temp.py
# @Software: PyCharm

#The program:
#Writen by Chong LYU
#in 07/10/2018
#To do a Finite Radon Transform with a 3*3 image.

import numpy as np
import math as m
a = np.array([[3,1,4],
             [2,0,5],
             [4,2,1]])

print('The original image:')
print(a)

p = m.floor(m.sqrt(a.size))
b = np.zeros((p+1,p))

#Define impulse response
def delta(a):
    if a == 0:
        return 1
    else:
        return 0

#a(k,l) -- FRT --> b(i,j)
for i in range (0,p+1):
    for j in range(0, p):
       if i != p:
           for k in range (0,p):
               for l in range (0,p):
                   b[i][j] += a[k][l] * delta((l - k * i - j) % p)
       elif i == p:
           for l in range (0,p):
               b[i][j] += a[j][l]

print('After FRT:')
print(b)