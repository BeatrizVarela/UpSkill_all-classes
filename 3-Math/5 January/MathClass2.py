# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 08:46:29 2021

@author: Ana Beatriz Varela
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4,4,20)
y1 = x**2
y2 = x**2+2
y3 = 2*x**2
y4 = -2*x**2
y5 = x**2-4

a=1
b=0
c=-4

formula=(b**2)-(4*a*c)
formula=np.sqrt(formula)
x1=(-b+formula)/(2*a)
x2=(-b-formula)/(2*a)
print("y5 intersecta X nos pontos",x1,"e",x2)

plt.plot(x, y1, '-b')
plt.plot(x, y2, '-r')
plt.plot(x, y3, '-g')
plt.plot(x, y4, '-y')
plt.plot(x, y5, '-c')

plt.xlabel('x')
plt.ylabel('y')
plt.grid()

plt.show()

'''
Exercise 1 (page 31)
'''
import matplotlib.pyplot as plt

x = np.linspace(-5,5,10)
y = 3**2/3

plt.hlines(y, xmin = -4, xmax = 4, label= 'y=3**2/3')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()

plt.show()

'''
Exercise 2
'''
import matplotlib.pyplot as plt

x = np.linspace(-4,4,20)
y = x**2

plt.plot(x, y, label= 'y=x**2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()

plt.show()

'''
Exercise 3
'''
import matplotlib.pyplot as plt

x = np.linspace(-5,5,20)
y = (4/3)*x**2*1 #4/3*x**2*y, y=1

plt.plot(x, y, label= 'y=(4/3)*x**2*y')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()

plt.show()

'''
Exercise 4
'''
import matplotlib.pyplot as plt

x = np.linspace(-2,2,200)
y = (x**3*1**4*2*x**2*1**3)**2 # = 2*x**10*y**14

plt.ylim(0,4)
plt.plot(x, y, label= 'y=2x**10*y**14')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()

plt.show()

'''
Exercise 5
'''
import matplotlib.pyplot as plt

x = np.linspace(-5,5,200)
y = 2*x*(x**4*1**4)**4

plt.ylim(-5,5)
plt.plot(x, y, label= 'y=2x*(x**4*y**4)**4')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()

plt.show()

'''
Exercise 6
'''
import matplotlib.pyplot as plt

x = np.linspace(-5,5,10)
y = 3**4/3

plt.hlines(y, xmin = -4, xmax = 4, label= 'y=3**4/3')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()

plt.show()

'''
Exercise 7
'''
import matplotlib.pyplot as plt

x = np.linspace(-50,50,20)
y = (x*1**3)/4 # y=1

plt.plot(x, y, label= 'y=xy**3/4')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()

plt.show()

'''
Exercise 8
'''
import matplotlib.pyplot as plt

x = np.linspace(-50,50,20)
y = (x*1**3)/4*x*1 # y=1

plt.plot(x, y, label= 'y=xy**3/4xy')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()

plt.show()

'''
Exercise 9
'''
(((u**2)(v**2))*(2(u**4)))**3=(2(u**6)(v**2))**3=(2**3)(u**(6*3))(v**(2*3))=8(u**18)(v**6)

x = 8(u**18)(v**6)

'''
Exercise 10
'''
((3v(u**5))*(2(v**3)))/((u(v**2))*(2(u**3)v))=(6(v**4)(u**5))/(2(u**4)(v**3))=3vu

v=1
3u == u=1
3v

import matplotlib.pyplot as plt
import numpy as np

u=np.linspace(-5,5,100)
y=3*u
plt.plot(u,y,label="y=3u or y=3v")
plt.legend()

plt.show()

'''
Logarithms (page 36)
Write each equation in its exponential form: 

Exercise 1
'''
import math

2 = math.log(7)x
print(7**2)             # 49

'''
Exercise 2
'''
import math

3 = math.log(10)x+8
a = 10**3
print(a - 8)            # 992

'''
Exercise 3
'''
import math

math.log(5)125=x
print(math.log(125,5))  # 3

'''
Rewrite into logarithms:

Exercise 1
'''
import math

2**4 = 16
print(math.log(16,2))   # 4

'''
Exercise 2
'''
import math

x = math.sqrt(64)       # 8
print(math.log(8,64))   # 0.5

'''
Exercise 3
'''
import math

x = math.e**4                   # 54.59815003314423
print(math.log(54.60,math.e))   # 4.000033882750859

'''
Logarithms – exercises (page 38)

Exercise 1
'''
import numpy as np

print((0.6**(np.sqrt(3))))      # 0.4128066587835584

'''
Exercise 2
'''
import numpy as np

print(((np.e)**3.2))            # 24.53253019710935

'''
Exercise 3
'''
print(((1.0005)**400))          # 1.2213417098970276

'''
Exercise 4
'''
log4(64) = log4((4**3)) = 3,  # 3

'''
Exercise 5
'''
import numpy as np

ln 1 = 0 
print((np.log(1)))              # 0.0

'''
Exercise 6
'''
import numpy as np

print((np.log((np.sqrt(7)))))   # 0.9729550745276567

'''
Exercise 7
'''
log5(25) = log5(5**2)         # 2

'''
Exercise 8
'''
log3((1/81)) = log3(1) - log3(81) = 0 - log3(3**4)    # -4

'''
Exercise 9
'''
ln((e**-2))                   # -2

'''
Exercise 10
'''
import numpy as np

log7(3) = log10(3)/log10(7)
print((np.log10(3)/np.log10(7))) # 0.5645750340535797

'''
Exercise 11
'''
log2(1/2) = log(2**-1)          # -1

'''
Exercise 12
'''
import numpy as np

log15(42) = log10(42)/log10(15)
print((np.log10(42)/np.log10(15))) # 1.3802069166820061

'''
Exercise 13
'''
import matplotlib.pyplot as plt
import numpy as np

log10(10x) = log10(10) + log10(x) = 1 + log10(x)

x = np.linspace(1,100,1000)
y = 1+np.log10(x)
plt.plot(x,y, "-g")
plt.grid()

plt.show()                          # 1+log⁡(x)

'''
Exercise 14
'''
ln(((x*y)/z)) = ln(x*y)-ln(z)     # ln(x)+ln(y)-ln(z)

'''
Exercise 15
'''
import matplotlib.pyplot as plt
import numpy as np

log4(4(x**2)) = log4(4)+log4(x**2)      # 1+2log4(x) = 1+2*(log10(x)/log10(4))

x = np.linspace(1,100,1000)
y = 1+2*((np.log10(x))/(np.log10(4)))
plt.plot(x,y)
plt.grid()

plt.show()

'''
Exercise 16
'''
import matplotlib.pyplot as plt
import numpy as np

log3(sqrt(x-2))=log3((x-2)**(1/2))        # (1/2)*log3(x-2) = (1/2)*((log2(x-2))/log2(3))

x = np.linspace(3,100,1000)
y = (1/2)*((np.log2(x-2))/np.log2(3))
plt.plot(x,y)
plt.grid()

plt.show()

'''
Exercise 17
'''
import matplotlib.pyplot as plt
import numpy as np

ln((sqrt(3x))/7)=ln((3x)**(1/2))-ln(7)     # (1/2)(ln(3x))-ln(7)

x = np.linspace(1,100,1000)
y = (1/2)*(np.log(3*x))-np.log(7)
plt.plot(x,y)
plt.grid()

plt.show()

'''
Radicals – exercises (page 43)

Exercise 1
'''
3sqrt(12)=3sqrt(2*2*3)=3*2sqrt(3)
# 6sqrt(3)

'''
Exercise 2
'''
6sqrt(128)=6sqrt(2*64)=6*2sqrt(32)=12sqrt(2*16)=12*2sqrt(8)=24sqrt(2*4)
# 24*2sqrt(2)

'''
Exercise 3
'''
7sqrt(128)=7*2*2*2sqrt(2)
# 56sqrt(2)

'''
Exercise 4
'''
-8sqrt(392)=-8sqrt(2*196)=-8*2sqrt(98)=-16sqrt(98)=-16sqrt(2*49)=-16sqrt(2*7*7)=-16*7sqrt(2)
# -112sqrt(2)

'''
Exercise 5
'''
-7sqrt(63)=-7sqrt(7*9)=-7sqrt(7*3*3)=-7*3sqrt(7)
# -21sqrt(7)

'''
Exercise 6
'''
sqrt(192n)=sqrt(2*96n)=2sqrt(48n)=2sqrt(2*24n)=4sqrt(12n)
# 8sqrt(3n)

import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1,10,100)
y = 8*np.sqrt(3*n)
plt.plot(n,y,label='y=8sqrt(3n)')
plt.legend()
plt.grid()

plt.show()

'''
Exercise 7
'''
sqrt(343b)=sqrt(7*49b)
# 7sqrt(7b)

import matplotlib.pyplot as plt
import numpy as np

b = np.linspace(1,10,100)
y = 7*np.sqrt(7*b)
plt.plot(b,y,label='y=7sqrt(7b)')
plt.legend()
plt.grid()

plt.show()

'''
Exercise 8
'''
sqrt(192(n**2))=n*sqrt(2*96)=2n*sqrt(48)=2n*sqrt(2*24)=4n*sqrt(12)
# 8nsqrt(3)

import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1,10,100)
y = 4*n*np.sqrt(3)
plt.plot(n,y,label='y=8n*sqrt(3)')
plt.legend()
plt.grid()

plt.show()

'''
Exercise 9
'''
sqrt(100(n**3))=sqrt(10**2(n**2)n)
# 10nsqrt(n)

import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1,10,100)
y = 10*n*np.sqrt(n)
plt.plot(n,y,label='y=10n*sqrt(n)')
plt.legend()
plt.grid()

plt.show()

'''
Exercise 10
'''
sqrt(200(a**3))=sqrt(2*100*(a**2)*a)
# 10a*sqrt(2a)

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,10,100)
y = 10*x*np.sqrt((2*x))
plt.plot(a,y,label='y=10a*sqrt(2a)')
plt.legend()
plt.grid()

plt.show()

'''
Multiple functions for comparisons
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,3,10)
y1 = 2**x 
y2 = 3**x
y3 = (2**x) + 4
y4 = (2**(x+1))

plt.plot(x,y1, 'm', label= '2**x')  
plt.plot(x, y2, '-b', label= '3**x')
plt.plot(x, y3, '-r', label= '(2**x) +4')
plt.plot(x, y4, label= '(2**(x+1))')

plt.title('Exponential function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()

plt.show()

'''
Logarithms functions
'''
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(1,100,200)
y1=np.sqrt(x)
plt.plot(x,y1,'-m',label='y=sqrt(x)')
plt.legend()
plt.grid()
plt.show()

x=np.linspace(1,100,200)
y1=np.log(x)
plt.plot(x,y1,'-m',label='y=log(x)')
plt.legend()
plt.grid()
plt.show()

# *********************************