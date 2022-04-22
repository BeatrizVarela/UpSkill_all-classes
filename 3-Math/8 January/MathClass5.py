# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 08:39:43 2021

@author: Ana Beatriz Varela
"""

'''
Exercise 1 (page 1)

Which graphs show relations that are functions:
'''

# Function
# NOT a function
# Function
# Function
# NOT a function

'''
Exercise 2 (page 2)

Given the following graph, evaluate f(−1):
'''
    # f(−1), aprox. y=1

'''
Solve for f(x)=3:
'''
    # f(x)=3, aprox. x=6


'''
Given the following graph, evaluate f(0):
'''
    # f(0), aprox. y=1
    
'''
Solve for f(x)=−3:
'''
    # f(x)=-3, aprox. x=-2 e 2

'''
Evaluate the expressions, given functions f, g, and h:
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4.2,4.5,25)
f = (3*x)-2
g = 5-(x**2)
h = -2*(x**2)+(3*x)-1

plt.plot(x, f, label='f(x)=3x-2')
plt.plot(x, g, label='g(x)=5-x**2')
plt.plot(x, h, label='h(x)=-2x**2+3x-1')

axes = plt.gca()
axes.set_ylim([-5,7])
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()

plt.show()

'''
3f(1)-4g(-2)
'''
x1 = 1
f = 3*x1-2
x2 = -2
g = 5-(x2)**2

func = (3*f)-(4*g)
print(func)

plt.hlines(func, xmin=-5, xmax=5, label="3f(1)-4g(-2) = -1")
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()

plt.show()

'''
f(7/3)-h(-2)
'''
x1 = (7/3)
f = 3*x1-2
x2 = -2
h = -2*(x2**2)+(3*x2)-1

func = (f)-(h)
print(func)

plt.hlines(func, xmin=-5, xmax=5, label="f(7/3)-h(-2) = 20")
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()

plt.show()

'''
Plot the following functions on Python

𝑦=𝑥^4 +3
𝑦=𝑥^5+4x
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2,2,20)
y1 = (x**4)+3
y2 = (x**5)+(4*x)

plt.plot(x, y1, label='y=x**4+3')
plt.plot(x, y2, label='y=x**5+4*x')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='lower right')
plt.grid()

plt.show()

'''
𝑦=√𝑥 +6
𝑦=∛𝑥
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-15,15,10)

y3 = (np.sqrt(x))+6
y4 = 3*(np.sqrt(x))

plt.plot(x, y3, label='y=np.sqrt(x)+6')
plt.plot(x, y4, label='y=3*np.sqrt(x)')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='lower right')
plt.grid()

plt.show()

'''
𝑦=tan⁡𝑥
𝑦=sin⁡〖(2𝑥〗) +4
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-(np.pi/2),np.pi/2,100)
# np.pi because the graph's values are tan and sin

y5 = np.tan(x)
y9 = (np.sin(2*x))+4

plt.plot(x, y5, label='y=np.tan(x)')
plt.plot(x, y9, label='y=np.sin(2*x)+4')

axes = plt.gca()
axes.set_ylim([-4,7])

plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='lower right')
plt.grid()

plt.show()

'''
𝑦=−𝑥+2
𝑦=−3𝑥+2
𝑦=−〖2𝑥〗^2+1
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1.5,15)

y6 = (-x)+2
y7 = ((-3)*x)+2
y8 = (-2*(x**2))+1

plt.plot(x, y6, label='y=-x+2')
plt.plot(x, y7, label='y=-3*x+2')
plt.plot(x, y8, label='y=(-2*x)**2+1')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='lower right')
plt.grid()

plt.show()


'''
Determine the nth term of the sequence:
    
a)
seq=(2,4,6,8,10,...)

arrythmetic seq d=2
an = a1+(n-1)d = 2+(n-1)*2 = 2+2n-2 = 2n
an = 2n
'''
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1,20,20)
an = 2*n

plt.scatter(n,an, label='(2, 4, 6, 8, 10,...)')
plt.legend(loc='upper left')
plt.grid()
plt.show()

'''
b)
seq=(1,3,5,7,9,...)

arrythmetic seq d=2
an = a1+(n-1)d = 1+(n-1)*2 = 1+2n-2 = 2n-1
an = 2n-1
'''
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(0,20,20)
an = 2*n-1

plt.scatter(n,an, label='(1, 3, 5, 7, 9,...)')
plt.legend(loc='upper left')
plt.grid()
plt.show()

'''
c)
seq=(99,199,299,399,499,...)

arrythmetic seq d=100
an = a1+(n-1)d = 99+(n-1)*100 = 99+100n-100 = 100n-1
an = 100n-1
'''
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(0,20,20)
an = 100*n-1

plt.scatter(n,an, label='(99, 199, 299, 399, 499,...)')
plt.legend(loc='upper left')
plt.grid()
plt.show()

'''
d)
seq=(3,-5,7,-9,11,...) 

an = (2n+1)*(-(-1)**n)
'''
import numpy as np
import matplotlib.pyplot as plt

n=np.linspace(1,20,20)
an=(2*n+1)*(-(-1)**n)

plt.scatter(n,an, label='(3 ,-5, 7, -9, 11,...)')
plt.legend(loc='upper left')
plt.grid()
plt.show()

'''
e)
seq=(2,(3/2),(4/3),(5/4),(6/5),...)

two arrythmetic seq dividing
d = 1
an = ax/ay
ax = 2+(n-1)*1 = 1+n
ay = 1+(n-1)*1 = n

an = (1+n)/n
'''
import numpy as np
import matplotlib.pyplot as plt

n=np.linspace(1,20,20)
an=(1+n)/n

plt.scatter(n,an, label='(2, (3/2), (4/3), (5/4), (6/5),...)')
plt.legend(loc='upper left')
plt.grid()
plt.show()

'''
f)
seq=(1,4,9,16,25,...)

two arrythmetic seq mult
d = 1
an = ax*ay
ax = n
ay = n
an = n*n
an = n**2
'''
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1,20,20)
an = n**2

plt.scatter(n,an, label='(1, 4, 9, 16, 25,...)')
plt.legend(loc='upper left')
plt.grid()
plt.show()

'''
g)
seq=(0,2,6,12,20,...)

two arrythmetic seq mult
an = ax*ay
ax = (-1+n)
ay = n
an = (-1+n)*n
'''
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1,20,20)
an = (-1+n)*n

plt.scatter(n,an, label='(0,2,6,12,20,...)')
plt.legend(loc='upper left')
plt.grid()
plt.show()

'''
h)
seq=(1,(2/3),(4/9),(8/27),(16/81),...)

two geometric seq diving
an = ax/ay
rax = 2/1 = 4/2 = 2
ray = 3/1 = 9/3 = 3
ax = 1*2**(n-1) = 2**(n-1)
ay = 1*3**(n-1) = 3**(n-1)
an = (2**(n-1))/(3**(n-1)) = (2/3) ** (n-1)
'''
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1,20,20)
an = (2/3)**(n-1)

plt.scatter(n,an, label='(0,2,6,12,20,...)')
plt.legend(loc='upper left')
plt.grid()
plt.show()

'''
i)
seq=(6,12,20,30,42,...)
'''
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1,20,20)
an = ((n+1)**2+(n+1))

plt.scatter(n,an, label='(6,12,20,30,42,...)')
plt.legend(loc='upper left')
plt.grid()
plt.show()

'''
j)
seq=((2/3), (3/(2*4)), (4/(3*5)), (5/(4*6)), (6/(5*7)),...)

an = ax/(ay*az)
ax = n+1
ay = n
az = n+3
an((n+1)/n*(n+2)) = ((n+1)/(n**2+2n))
'''
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1,20,20)
an = ((n+1)/(n*(n+2)))

plt.scatter(n,an, label='((2/3), (3/(2*4)), (4/(3*5)), (5/(4*6)), (6/(5*7)),...)')
plt.legend(loc='upper left')
plt.grid()
plt.show()

'''
k)
seq=(0,(1/3),0,(1/3),0,...)

an = (-1/6)*sin((pi/2)+pi*n)+(1/6)
'''
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(-7,7,15)
an = (-1/6)*np.sin((np.pi/2)+np.pi*n)+(1/6)

plt.scatter(n,an, label='(0,(1/3),0,(1/3),0,...)')
plt.legend(loc='upper left')
plt.grid()
plt.show()

'''
l)
seq=(-(1/2),(2/5),-(3/8),(4/11),-(5/14),...)

an = ((-1)**n)*((n)/(2*n+(n-1)))
'''
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1,20,20)
an = ((-1)**n)*((n)/(2*n+(n-1)))

plt.scatter(n,an, label='(-(1/2),(2/5),-(3/8),(4/11),-(5/14),...)')
plt.legend(loc='lower right')
plt.grid()
plt.show()

'''
Find the sum of the first five terms of the sequence:

a)
an+1= an-1.5
a1 = 3.5
'''
seq = [3.5]
soma = seq[0]
for n in range(4):
    an1 = seq[n]-1.5
    soma+= an1
    seq.append(an1)
    # print(seq)
    
print("The sum of the first five members are",soma)     # 2.5

'''
b)
an+1= (1/an)-1
a1 = 5
'''
seq = [5]
soma = seq[0]
for n in range(4):
    an1 = (1/seq[n])-1
    soma+= an1
    seq.append(an1)
    
print("The sum of the first five members are",soma)     # -1.1867521367521365

'''
c)
    an+1=(an^2-n**2)/2
    a1=1
'''
seq=[1]
soma=seq[0]
for n in range(4):
    an1=((seq[n]**2)-((n+1)**2))/2
    soma+=an1
    seq.append(an1)
    
print("The sum of the first five members are",soma)     # -8.375

'''
d)
    an+1=sqrt(an)
    a1=65.536
'''
import numpy as np

seq=[65536]
soma=seq[0]
for n in range(1,5):
    an1=np.sqrt(seq[(n-1)])
    soma+=an1
    seq.append(an1)
    
print("The sum of the first five members are",soma)     # 65814.0

'''
e)
    an+1=(2**(n+1))*(((n+1)**2)-(2*an))
    a1=1
'''
seq=[1]
soma=seq[0]
for n in range(1,5):
    an1=(2**n)*((n**2)-(2*seq[(n-1)]))
    soma+=an1
    seq.append(an1) 
    
print("The sum of the first five members are",soma)     # 13927

'''
Factorials
'''
import math

print(math.factorial(2))    # 2
print(math.factorial(3))    # 6
print(math.factorial(10))   # 3628800

# *********************************
import math

x = np.deg2rad(30)          # cos(30)
n = 0
N = 25
result = 0
sign = 1.0

while n < N:
    term = sign*x**(2*n)/math.factorial(2*n)
    result = result + term
    n +=1
    sign = -sign
print(result)               # 0.86
print((np.sqrt(3))/2)       # 0.86
    
# *********************************
import math

x = np.deg2rad(90)          # cos(90)
n = 0
N = 25
result = 0
sign = 1.0

while n < N:
    term = sign*x**(n)/math.factorial(n)
    result = result + term
    n +=2
    sign = -sign
print(result)               # 4.253977785846482 e-17
    
# *********************************
import matplotlib.pyplot as plt
import numpy as np

x = 1.0
n = 50
a = n/n+1
data = []

for i in range(n):
    x1 = i/(i + 1)
    if abs(x1 - x) < 1.e-3:
        print('a = {a}, n = {i}, result is {x}.'.format(a=a, i=i, x=x))
        last_index = i
        break
    else:
        pass
    x = x1
    data.append([i,x])
    last_index = n

plt.scatter(*zip(*data))
plt.hlines(y=1,xmin=0,xmax=last_index)
plt.xlim(0, last_index)

# *********************************