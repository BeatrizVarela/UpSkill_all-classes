# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 09:08:04 2021

@author: Ana Beatriz Varela
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,0,5)
x1 = 0
x2 = np.linspace(0,4,5)
y = x-3
y1 = 1
y2 = x+2

plt.plot(x, y, '-r', label='y=x-3')
plt.plot(x1, y1, '-g', label='y=1')
plt.plot(x2, y2, '-m', label='y=x+2')

plt.title('Linear graphs')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()

plt.show()

# *********************************

import matplotlib.pyplot as plt
import numpy as np 

x = [-5,5]
m = [1,2,3,5]
b = [-2,3/4,2,1]
color = ['g', 'r', 'k', 'm']
for i in range(0,len(m)):
    y = m[i]*np.array(x) + b[i]
    plt.plot(x,y,label='y=%sx+%s' %(m[i],b[i]), color=color[i] )
    
plt.axis('auto')
plt.xlim(x)
plt.ylim(x)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
axis = plt.gca()
plt.legend(prop={'size':15})
plt.title('Generic plot')

plt.show()

# *********************************

import matplotlib.pyplot as plt

plt.hlines(y = 3, xmin = 1, xmax = 10, colors='r')
plt.vlines(x = 6, ymin = 1, ymax = 10, colors='r')

plt.title('Constant graphs ')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()

plt.show()

# *********************************
# Exercise 1 (page 18)
# *********************************

import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-8,5)

f = x-5
g = 4*x+2
fg = 5*x-3

plt.plot(x,f, label="f(n)=n-5")
plt.plot(x,g, label="g(n)=4n+2")
plt.plot(x,fg, label="(f+g)(n)")

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')

plt.show()

n = -8
fgn = 5*n-3
print("The point is located at",fgn,"y.")   # -43

# *********************************
# Exercise 2
# *********************************

import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-8,5)

g = 3*x-2
h = 4*x-2
gh = 7*x-4

plt.plot(x,g, label="g(a)=3a-2")
plt.plot(x,h, label="h(a)=4a-2")
plt.plot(x,gh, label="(g+h)(a)")

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')

plt.show()

a = -10
gha = 7*a-4
print("The point is located at",gha,"y.")   # -74

# *********************************
# Exercise 3
# *********************************

import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-8,5)

g = x**2-2
h = 2*x+5
gh = x**2+2*x+3

plt.plot(x,g, label="g(x)=x**2-2")
plt.plot(x,h, label="h(x)=2x+5")
plt.plot(x,gh, label="(g+h)(x)")

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')

plt.show()

x1 = -6
g = x1**2-2
h = 2*x1+5
ghx = g+h
print("The point is located at",ghx,"y.")   # 27

# *********************************
# Exercise 4
# *********************************

import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-8,8)

h = x+5
g = 3*x-5
hg = 3*x**2+10*x-25

plt.plot(x,g, label="h(t)=t+5")
plt.plot(x,h, label="g(t)=3t-5")
plt.plot(x,hg, label="(hg)(t)")

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')

plt.show()

t = 5
h = t+5
g = 3*t-5
ght = g*h
print("The point is located at",ght,"y.")   # 100

# *********************************
# Exercise 5
# *********************************

import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-6,10,1000)

h = 2*x-1
g = 3*x-5
hg = h/g

plt.plot(x,g, label="h(n)=2n-1")
plt.plot(x,h, label="g(n)=3n-5")
plt.plot(x,hg, label="(hg)(n)")

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')

plt.ylim(-10,10)

plt.show()

n = 0
h = 2*n-1
g = 3*n-5
hgn = h/g
print("The point is located at",hgn,"y.")   # 0.2

# *********************************
# Exercise 6
# *********************************

import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-1,1)

g = x-3
h = (-3*x)**3+6*x
gh = (-3*x)**3+7*x-3

plt.plot(x,g, label="g(t)=t-3")
plt.plot(x,h, label="h(t)=-3t**3+6t")
plt.plot(x,gh, label="(gh)(t)")

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')

plt.show()

t = 1
g = t-3
h = -3*(t)**3+6*t
ght = g+h
print("The point is located at",ght,"y.")   # 1

# *********************************
# Continuous polynomial functions types 
# *********************************
'''
Quadratic Function
'''
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-10,10,10)
y1 = x**2

plt.plot(x, y1, '-r')
plt.show()

'''
Cubic Function
'''
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-10,10,10)
y1 = -3*x**3+6*x

plt.plot(x, y1, '-b')
plt.show()

'''
Quartic Graph
'''
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-10,10,10)
y1 = -3*x**4+6*x+2*x

plt.plot(x, y1, '-b')
plt.show()

# *********************************
# Maximum and minimum values 
# *********************************
'''
Quadratic Function
'''
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-10,10,10)
y1 = x**2

plt.plot(x, y1, '-r')

#

x = np.linspace(-10,10,10)
y1 = -x**2

plt.plot(x, y1, '-g')
plt.show()

'''
Cubic Function
'''
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(-10,10,10)
y1 = -3*x**3+6*x

plt.plot(x, y1, '-b')
plt.show()

# *********************************
# Discrete functions
# *********************************

import matplotlib.pyplot as plt

x = [-3,-2,-1,0,1,2,3]
y = [8,4,2,0,2,4,8]
color = ['g', 'r', 'k', 'm', 'k', 'r', 'g']
for i in range(0,len(x)):
    plt.plot(x[i],y[i], 'o', color=color[i] )


plt.title(' Discrete function')
plt.legend(loc='upper left')
plt.grid()

plt.show()

# *********************************
# Polynomial regression 
# *********************************

import numpy
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 8))

myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.grid()
plt.show()

# *********************************
# Exercise - Linear regression  
# *********************************

import numpy
import matplotlib.pyplot as plt

x = [2400,2650,2350,4950,3100,2500,5106,3100,2900,1750]
y = [41200,50100,52000,66000,44500,37700,73500,37500,56700,35600]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 1))
print(mymodel)
# Linear regression equation: y = 9.774 x + 1.937e+04
# Slope = 9.774
# y-intersect = 1.937e+04

myline = numpy.linspace(-100, 5200, 75000)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.grid()

plt.show()

# *********************************
# Plotting discrete functions using Lists    
# *********************************

import matplotlib.pyplot as plt

x = [1, 2 ,3 ,4 ,5]
y1 =[1 ,2, 3, 4, 5]

plt.plot(x, y1, '-b', label= 'y = x')
plt.title(' Discrete function using lists')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()

plt.show()

# *********************************
# Plotting discrete functions using Tuples    
# *********************************

import matplotlib.pyplot as plt

x =(1,2,3,4,5)
y1 = (1,2,3,4,5)

plt.plot(x,y1,'or' ,label= 'y = x')  
plt.plot(x,y1,'b', label= 'y = x') 
plt.title(' Discrete function using tuples')
plt.legend(loc='upper left')
plt.grid()

plt.show()

# *********************************
# Plotting functions using Dictionaries  
# *********************************

import matplotlib.pyplot as plt

x1 = {'x':[1,2,3,4,5], 'y1':[1,2,3,4,5] }

plt.plot('x', 'y1', '-b', label= 'y = x', data=x1)
plt.title(' Discrete function using dictionaries')
plt.legend(loc='upper left')
plt.grid()

plt.show()

# *********************************