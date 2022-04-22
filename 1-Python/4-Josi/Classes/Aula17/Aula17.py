# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 08:44:50 2020

@author: Ana Beatriz Varela
"""

# ************************
# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/
# ************************

# ************************
# Aula 18
# ************************

# Nested for (não é boa prática)
for i in range(5):
    for j in range(6):
        print("Josi")
    print("Bernardo")
    
# ************************
 
import pandas as pd
import numpy as np

print(dir(pd))     
print(pd.__version__)
        
x = np.array([[-1,3],[4,2]])
y = np.array([[1,2],[3,4]])
z = np.dot(x,y)

print(z)

# ************************

print(np.log(-1))       # NaN - Not a Number



























