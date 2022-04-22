# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 08:46:50 2021

@author: Ana Beatriz Varela
"""

'''
Exercise 1 (page 7)
'''
import numpy as np
import math

y = 24*(np.pi)/180
print(y)                                # angulo em radianos
print(np.deg2rad(24))                   # angulo em radianos

print(13/np.sin(y))                     # valor de x = hipotenusa
print(13/math.sin(math.radians(24)))    # valor de x = hipotenusa
# 31.96

'''
Exercise 2
'''
import numpy as np

y = 52.3*(np.pi)/180
print(y)                                # angulo em radianos
print(np.deg2rad(52.3))                 # angulo em radianos

print(5/np.cos(y))                      # valor de x = hipotenusa
# 8.17

'''
Exercise 3
'''
import numpy as np

y = np.deg2rad(71)                      # angulo em radianos

print(9*np.tan(y))                      # valor de x = cateto
# 26.13

'''
Exercise 4
'''
import numpy as np

y = np.deg2rad(63)                    # angulo em radianos

print(7.6/np.cos(y))                  # valor de x = hipotenusa
# 16.74

'''
Exercise 1 (page 11)
'''
import numpy as np

x = np.arccos(4/7)                   # calculo de cos -1
y = np.rad2deg(x)                    # angulo em graus

print(y)                             # 55.15

'''
Exercise 2
'''
import numpy as np

x = np.arctan(12/13)                 # calculo de tan -1
y = np.rad2deg(x)                    # angulo em graus

print(y)                             # 42.7

'''
Exercise 3
'''
import numpy as np

x = np.arctan(16/10)                 # calculo de tan -1
y = np.rad2deg(x)                    # angulo em graus

print(y)                             # 57.99

'''
Exercise 4
'''
import numpy as np

x = np.arctan(5.6/15.3)              # calculo de tan -1
y = np.rad2deg(x)                    # angulo em graus

print(y)                             # 20.10

# *********************************
import numpy as np
np.set_printoptions (precision=2)
np.set_printoptions (formatter={"float":'{:0.2f}'.format})

a = np.array ([0,30,45,60,90])
print('Sine of different angles:') 
# Convert to radians by multiplying to pi/180
print(np.sin(a*np.pi/180), "\n")

print("Cosine values for angles in array:")
print(np.cos(a*np.pi/180), " \n")
print('Tangent values for given angles:')
print(np.tan(a*np.pi/180))

'''
Sine of different angles:
[0.00 0.50 0.71 0.87 1.00] 

Cosine values for angles in array:
[1.00 0.87 0.71 0.50 0.00]  

Tangent values for given angles:
[0.00 0.58 1.00 1.73 16331239353195370.00]
'''

'''
Funcoes Periodicas
'''
import numpy as np
import matplotlib.pyplot as plt

values = np.linspace(-(2*np.pi),2*np.pi,20)
cos_values = np.cos(values)
sin_values = np.sin(values)

plt.plot(cos_values, color= "blue", marker = "*")
plt.plot(sin_values, color= "red")
plt.show()

'''
cos(x) in degrees
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi,2*np.pi,40)
x1 = np.rad2deg(x)
y = np.cos(x)

plt.plot(x1,y)
plt.xlabel("degrees")
plt.ylabel("cos(x)")

'''
cos(x) in radians
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi,2*np.pi,40)
y = np.cos(x)

plt.plot(x,y)
plt.xlabel("radians")
plt.ylabel("cos(x)")

# *********************************
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,30)
y1 = np.sin(x)
y2 = 2*np.sin(x)
y3 = np.sin(x+1)
y4 = np.sin(x)+1
y5 = -np.sin(x)

plt.plot(x, y1, label='y = sin(x)')
plt.plot(x, y2, label='y = 2.sin(x)')
plt.plot(x, y3, label='y = sin(x+1)')
plt.plot(x, y4, label='y = sin(x)+1')
plt.plot(x, y5, label='y = -sin(x)')

plt.xlabel("radians")
plt.ylabel("sin(x)")
plt.legend(loc='lower right')
plt.grid()

'''
Exercise 1 (page 21)
'''
import numpy as np
import matplotlib.pyplot as plt

'''
radians
'''
x = np.linspace(-2*np.pi,2*np.pi,100)
y1 = 4 + 0.5*np.sin(x)
y2 = -4*np.cos(3*x-np.pi)

plt.plot(x, y1, label='y = 4+0.5*sin(x)')
plt.plot(x, y2, label='y = -4cos(3x-pi)')

plt.xlabel("radians")
plt.ylabel("sin(x)")
plt.legend(loc='lower right')
plt.grid()

'''
degrees
'''
x = np.linspace(-2*np.pi,2*np.pi,100)
x1 = np.rad2deg(x)
y1 = 4 + 0.5*np.sin(x)
y2 = -4*np.cos(3*x-np.pi)

plt.plot(x1, y1, label='y = 4+0.5*sin(x)')
plt.plot(x1, y2, label='y = -4cos(3x-pi)')

plt.xlabel("radians")
plt.ylabel("sin(x)")
plt.legend(loc='lower right')
plt.grid()

'''
samples
'''
x = np.linspace(-2*np.pi,2*np.pi,100)
y1 = 4 + 0.5*np.sin(x)
y2 = -4*np.cos(3*x-np.pi)

plt.plot(y1, label='y = 4+0.5*sin(x)')
plt.plot(y2, label='y = -4cos(3x-pi)')

plt.xlabel("radians")
plt.ylabel("sin(x)")
plt.legend(loc='lower right')
plt.grid()

# What is the period of these functions?
# What is the amplitude?
# How many samples (minimum amount) is needed to see the smoothing charts?

'''
minimum amount = 25 pt for the first charts and then increases 
4 times the number of pt
so, the number of pt needed is 25*amplitude for a smoothing charts
'''

# *********************************