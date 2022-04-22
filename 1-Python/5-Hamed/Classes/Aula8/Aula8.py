# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 09:12:49 2020

@author: Ana Beatriz Varela
"""

# ************************
# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/
# ************************

# ************************
# Aula 8
# ************************

'''
MEAN

Arithmetic Mean (AM)
Geometric Mean (GM)
Harmonic Mean (HM)

Arithmetic Mean = Sum of values of a data set divided by number of values
Median = Middle value separating the greater and lesser halves of a data set
Mode = Most frequent value in a data set
'''

# MEAN
import statistics
import numpy as np

a = [4, 36, 45, 50, 75]
b = [1, 2, 2, 3, 4, 7, 9]
c = [6, 3, 9, 6, 6, 5, 9, 9, 3, 1]

print(statistics.mean(a))   # 42
print(np.mean(b))           # 4.0
print(np.mean(c))           # 5.7

# MODE
import statistics
from scipy import stats
import numpy as np

print(statistics.mode(a))      # 4
print(stats.mode(b))           # ModeResult(mode=array([2]), count=array([2]))
print(stats.mode(c))           # ModeResult(mode=array([6]), count=array([3]))

# MEDIAN
print(statistics.median(a))    # 45
print(statistics.median(b))    # 3
print(np.median(c))            # 6.0












# ************************

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

fig1, ax = plt.subplots()
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns = ["sl", "sw", "pl", "pw"])
df["t"] = iris.target

ax.scatter(df.pl, df.pw, c = df.t, cmap=plt.cm.Set1, edgecolor="k");
ax.set(xlabel="PL", ylabel="PW")

# ************************












