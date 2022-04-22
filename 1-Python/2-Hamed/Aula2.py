# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 08:39:28 2020

@author: Ana Beatriz Varela
"""

#************************

#Modules
import math            #math is a module
print(math.pi)         #3.141592653589793

import math as m       #m is math module
print(m.pi)            #3.141592653589793

#************************

#Sub-Module

#From module import sub-module/function/variables
from os import getcwd         #importing a sub-module
getcwd()

#From module import sub-module as new_name
from os import getcwd as gc   #renaming the sub-module
gc()


from math import pi
print(pi)
print(math.pi)
print(math.e)
print(e)                #ERROR: e was not imported; only pi

#************************

for i in range(10):
    print(i)
    print(i+1)
    
#************************

import numpy as np
import pandas as pd    #ERROR: pd is not being used
import matplotlib.pyplot as plt

data = np.array([-20, -3, -2, -1, 0, 1, 2, 3, 4])
plt.boxplot(data)

#Replace the below code with the other type of import modules and remove '.'
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
plt.boxplot(data)

#************************

#A bad way to use modules is to import everything
from math import *    # '*' means everything in the module
print(pi)

# Module A contains F function
# Module B contains F function too

# From A import *
# From B import *

# F(...)              #Does F belong to A or B?

# sum??
# from numpy import *
# sum??

#************************

import math
dir(math)

s = 'a'
dir(s)                # This tells what functions can be used with this type of variable (this case, a string)

# __doc__             # Magic function ('__xx__')

#************************
# Exercise 1
#************************

def my_func():
    """
    This is a custom function


    
    """
    print('Python')

my_func()

help(my_func)         # Shows the custom function
my_func??             # Show detailed info about the function

def square(a):
    "Returns the square of a"
    return a ** 2

#************************
# Exercise 2
#************************

import math
print(math.fmod(9, 4))             # 1.0, 9%4
print(math.gcd(30, 4))             # 2, greatest common divisor
print(math.fabs(-4))               # 4.0, float abs

import random
print(random.randint(1, 5))        # 4, random number between 1 to 5
print(random.choice([1, 5]))       # 5, random number between only 1 or 5

a = [1, 2, 3, 4]
random.shuffle(a)
print(a)                           # randomize arrangement of a

#************************

import sys
print(sys.version)
print(sys.platform)

import platform
platform.release()

#************************

import datetime
now = datetime.datetime.now()
print(now)                         # 2020-10-20 11:31:57.901997
print(now.year)                    # 2020
print(now.month)                   # 10
print(now.day)                     # 20
print(datetime.datetime.today())   # 2020-10-20 11:31:57.903997

#************************
# Exercise 3
#************************
# Print if the current minute is even or odd.

import datetime
now = datetime.datetime.now()
a = now.minute
if a % 2 == 0 :
    print('Minute is even.')
else :
    print('Minute is odd.')

# Other solution

import datetime
now = datetime.datetime.today()
a = now.minute
if a % 2 == 0 :
    print('Minute is even.')
else :
    print('Minute is odd.')

# Another solution

from datetime import datetime as dt
a = dt.today().minute
print('Current minute is', a)
if a % 2 == 0 :
    print('Minute is even.')
else :
    print('Minute is odd.')

# Odds and Evens #2

from datetime import datetime as dt
a = dt.today().minute
print('Current minute is', a)
for i in range(1, 61, 2) :
    if a == i:
        print('Minute is odd.')
        break
    else:
        print('Minute is even.')
        break

# Odds and Evens #3

from datetime import datetime as dt
a = dt.today().minute
print('Current minute is', a)

odds_list = [i for i in range(1, 60, 2)]
if a in odds_list:
    print('Minute is odd.')
else:
    print('Minute is even.')

#************************