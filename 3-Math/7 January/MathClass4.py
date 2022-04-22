# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 09:04:43 2021

@author: Ana Beatriz Varela
"""

'''
Sequences
'''
import numpy as np

n = np.linspace(1,5,5)
y1 = (2*n-1)
y2 = (-1)**n
y3 = n**2+1
y4 = 0.25*n
y5 = 3**n

print(y1)        # [1. 3. 5. 7. 9.]
print(y2)        # [-1.  1. -1.  1. -1.]
print(y3)        # [ 2.  5. 10. 17. 26.]
print(y4)        # [0.25 0.5  0.75 1.   1.25]
print(y5)        # [  3.   9.  27.  81. 243.]

# *********************************
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1,20,20)
an = 2*n-1
print(an)       # [ 1.  3.  5.  7.  9. 11. 13. 15. 17. 19. 21. 23. 25. 27. 29. 31. 33. 35. 37. 39.]

plt.scatter(n,an, label='an=2n-1')
plt.grid()
plt.legend()

plt.show()

# *********************************
import numpy as np
import matplotlib.pyplot as plt

seq = (0.25, 0.5, 0.75, 1)
d = 0.25
n = np.linspace(1, 20, 20)
an = 0.25+(n-1)*d
print(an)       # [0.25 0.5  0.75 1.   1.25 1.5  1.75 2.   2.25 2.5  2.75 3.   3.25 3.5 3.75 4.   4.25 4.5  4.75 5.  ]

plt.scatter(n,an, label='an=0.25n')
plt.xticks(n, list(range(20)))
plt.grid()
plt.legend()

plt.show()

# *********************************
import numpy as np

n = np.linspace(1,5,5)
y1 = [1, 3, 5, 7, 9]
y2 = [-1, 1, -1, 1, -1]
y3 = [2, 5, 10, 17, 26]
y4 = [0.25, 0.5, 0.75, 1, 1.25]
y5 = [3, 9, 27, 81, 243]

a1 = y1[0]+(n-1)*(y1[1]-y1[0])
a2 = y2[0]**n
a3 = n**y3[0]+1
a4 = y4[0]+(n-1)*(y4[1]-y4[0])
a5 = y5[0]**n

# an = a1+(n-1)*d

print(a1)       # (2*n - 1)
print(a2)       # (-1)**n
print(a3)       # n**2 + 1
print(a4)       # 0.25*n
print(a5)       # 3**n

# Python doesn't show the formula, only the final result

'''
Summations Σ
'''
soma = 0
for n in range(0,5):
    soma += 2*n + 1
    print(soma)
    # 1
    # 4
    # 9
    # 16
    # 25
    
print("\n")
print(soma)         # 25

# *********************************
import numpy as np

y = [1, 3, 5, 7, 9]
sn = (len(y)*(y[0]+y[4]))/2

print(sn)           # 25

# *********************************
import numpy as np

n = np.linspace(1,20,20)
an = 0.25*n
sn = (4*(an[0]+an[3]))/2

print(sn)           # 2.5

'''
Geometric progression

A geometric progression, or geometric sequence, is a sequence of numbers in which 
each consecutive term is found by multiplying the previous by a non-zero constant. 
G = (a,ax,ax2,...,axn), for some x ≠ 0

'''
sq = (an[0]*(1-3**n[4]))/(1-3)
print(sq)                       # 363.0

# or
sq=0
for q in range(1,6):
    sq+= 3**q
    
print(sq)                       # 363

# *********************************
import numpy as np

n = np.linspace(1,5,5)
an = 2*n-1
sn = 0

for n in range(0,5):
    sn+=2*n+1
print(sn)               # 25

# or
sn = (5*(an[0]+an[4]))/2
print(sn)               # 25.0

# or
print(np.sum(an))       # 25.0

'''
Mean
'''
import numpy as np

y = [1, 3, 5, 7, 9]
sn = (len(y)*(y[0]+y[4]))/2/len(y)
print(sn)                 # 5.0

# or
print(np.mean(y))         # 5.0

# or
print(np.sum(y)/len(y))   # 5.0

'''
Exercise (page 17)

Find the Σ (sum) of n = 1 -> 12 4(0.3)**n
r = a2/a1
'''
r = (4*(0.3**2))/(4*(0.3**1))
def seq_sum_geo(a1, n, n_max, r):
    sn = (a1*(0.3**n))*(1-(r**n_max))/(1-r)
    return sn
a1 = 4

print(seq_sum_geo(a1,1,12,0.3))     # 1.7142848032440001
print(seq_sum_geo(a1,0,12,0.3))     # 5.714282677480001

'''
Convergence
'''
import matplotlib.pyplot as plt

x = 1.0
n = 50
a = n/n+1
data = []

for i in range(n):
    x1 = i/(i + 1)
    if abs(x1 - x) < 1.e-3:
        print('a = {a}, n = {i}, result is {x}.'.format(a=a, i=i, x=x))
        # a = 2.0, n = 32, result is 0.96875.
        
        last_index = i
        break
    x = x1
    data.append([i,x])
    last_index = n

plt.scatter(*zip(*data))
plt.hlines(y=1, xmin=0, xmax=last_index)
plt.xlim(0, last_index)
plt.grid()

plt.show()

# *********************************
import matplotlib.pyplot as plt

x = 1.0
n = 50
data = []

for i in range(n):
    x1 = i/(i + 1)
    if abs(x1 - x) < 1.e-2:
        print('n = {i}, result is {x}.'.format(i=i, x=x))
            # n = 10, result is 0.9.
            
        last_index = i
        break
    x = x1
    data.append([i,x])
    print(i, x)
        # 0 0.0
        # 1 0.5
        # 2 0.6666666666666666
        # 3 0.75
        # 4 0.8
        # 5 0.8333333333333334
        # 6 0.8571428571428571
        # 7 0.875
        # 8 0.8888888888888888
        # 9 0.9
            
else:
    print('No convergence within {n} iterations.'.format(n=n))
    last_index = n
    
plt.scatter(*zip(*data))
plt.hlines(y=1, xmin=0, xmax=last_index)
plt.xlim(0, last_index)
plt.grid()

plt.show()

'''
Exercise (page 20)
Check if the sequence converges using python:
'''
import matplotlib.pyplot as plt

# if 0 < r < 1
def n_seq(a,r,n):
    print(a)                # 1
    print(r)                # 0.5
    seq_val=[]
    for i in range(1,(n+1)):
        seq = a*(r**i)
        seq_val.append(seq)
    return seq_val

n = 20
seq = n_seq(1, 0.5, n)      # (a, r, n)

plt.scatter(list(range(1,(n+1))),seq,label = 'an=a*r^n, 0<r<1')
plt.hlines(0,0,20)
plt.legend()
plt.grid()

plt.show()

# if r > 1
def n_seq(a,r,n):
    print(a)                # 1
    print(r)                # 2
    seq_val=[]
    for i in range(1,(n+1)):
        seq = a*(r**i)
        seq_val.append(seq)
    return seq_val

n = 20
sq = n_seq(1, 2, n)      # (a, r, n)

plt.scatter(list(range(1,(n+1))),sq,label = 'an=a*r^n,r=>1')
plt.ylim(0,1000)
plt.legend()
plt.grid()

plt.show()

"""
whilist r is between 0 and 1 there is a convergence to 0, but when r is 
higher than 1 there is no convergence, looking like an exponential function.
"""

# *********************************