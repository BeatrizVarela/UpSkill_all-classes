# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 08:44:33 2021

@author: Ana Beatriz Varela
"""

'''
Previous classes revisions
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,10)
y = x
plt.plot(x,y, "-o")
plt.grid()

plt.show()

# *********************************
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,10)
y = x
plt.plot(x,y, "-or")
plt.semilogy()
plt.grid()

plt.show()

# *********************************
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,10)
y = x
plt.plot(x,y, "-og")
plt.semilogx()
plt.grid()

plt.show()

# *********************************
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,10)
y = x
plt.plot(x,y, "-om")
plt.yscale("log")
plt.xscale("log")
plt.grid()

plt.show()

'''
Exercises (page 10)

a)
'''
import numpy as np
import matplotlib.pyplot as plt

# N = No e**2t

x = np.linspace(0,10,11)
y = 100*(np.exp(2*x))

plt.plot(x,y, "-og")
plt.xlabel('months')
plt.ylabel('bacteria population')
plt.hlines(1000000,0,10)
plt.semilogy()
plt.grid()

plt.show()

val = round((np.log((1000000/100))/2),2)
print("It takes",val,"months before the bacteria population reaches one million") # 4.61

'''
b)

i.
'''
import numpy as np
import matplotlib.pyplot as plt

M = np.linspace(0,10,11)
E = 1.74*(10**19)*(10**(1.44*M))

plt.plot(M,E)
plt.yscale('log')
plt.xticks(list(range(0,11)),list(range(0,11)))
plt.grid()
plt.show()

joules = 1.74*(10**19)*(10**(1.44*5))
print(f'The Earthquake of that magnitude released {joules:.2e} Joules')         # 2.76e+26

'''
ii.
'''
joulesTimesTwo = joules*2
m_list = list(np.linspace(4,6,10000))

for M in m_list:
    E = 1.74*(10**19)*(10**(1.44*M))
    if E >= joulesTimesTwo:
        break
print(f'The magnitude of the Earthquake was of {M:.2f} on the Richter scale')   # 5.21

'''
Find the n and A (slide 11)

n = (log(y2)-log(y1))/(log(x2)-log(x1))

eg: log(A) = 0.5 == A = 10**0.5
'''

'''
Consider the data (slide 12)
'''
import matplotlib.pyplot as plt
import numpy as np

x = [2,30,70,100,150]
y = [4.24,16.4,25.1,30.0,36.7]
plt.plot(x,y,"o")
plt.show()

logx = np.log10(x)
logy = np.log10(y)
print(np.poly1d(np.polyfit(logx,logy,1)))
plt.plot(logx,logy,'o')
plt.show()

'''
The data below obeys a power law y=A*(x**n).
Obtain the equation and select the correct statement.
(slide 13)
'''
import numpy as np
import matplotlib.pyplot as plt

x = [5,15,30,50,95]
y = [10,90,360,1000,3610]

plt.plot(x,y,"-o")
plt.show()
# n = (log(y2)-log(y1))/(log(x2)-log(x1))

# print(np.log10(y))      # [1.  1.95424251   2.5563025   3.   3.5575072]
y0 = np.log10(y[0])
# print(y0)               # 1.0
y1 = np.log10(y[1])
# print(y1)               # 1.954242509439325

# print(np.log10(x))      # [0.69897   1.17609126   1.47712125   1.69897   1.97772361]
x0 = np.log10(x[0])
# print(x0)               # 0.6989700043360189
x1 = np.log10(x[1])
# print(x1)               # 1.1760912590556813

n_y = y1-y0
# print(n_y)              # 0.954242509439325
n_x = x1-x0
# print(n_x)              # 0.4771212547196625
n = n_y/n_x
# print(n)                # 2.0

logx = np.log10(x)
logy = np.log10(y)
plt.plot(logx,logy,"-o")
plt.show()

print(np.poly1d(np.polyfit(logx,logy,1)))   # 2 x - 0.3979
result = 10**(-0.3979)
print(result)                               # 0.40003685104612496

# n = 2 e A = 2/5

# *********************************