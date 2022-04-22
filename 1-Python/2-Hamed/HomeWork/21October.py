# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 08:34:10 2020

@author: Ana Beatriz Varela
"""

# 1 - print first row
# 2 - print first column in single line
# 3 - print main diameter 1, 5, 9
# 4 - print another diameter 3 5 7
# 5 - Calculate Sum of rows
# 6 - Calculate Sum of columns

'''
Exercise 1
'''

m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print('First row is ', m[0])

'''
Exercise 2
'''

i = 0, 1, 2
for i in [0, 1, 2]:
    print(m[i][0], end=' ')

for i in range(3):
    print(m[i][0], end=' ')

for i in range(len(m)):
    print(m[i][0], end=' ')

'''
Exercise 3
'''

i = 0, 1, 2
for i in range(len(m)):
    print(m[i][i], end=' ')

'''
Exercise 4
'''

m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

j = 2

for i in range(3):
    print(m[i][j], end=' ')
    j -= 1

'''
Exercise 5
'''

m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

s=[sum(i) for i in m]
print (s)

'''
Exercise 6
'''

# import numpy as np
# m2 = np.array(m)
# m2.T

# i = 0, 1, 2
# print(sum(m[i]))


m1 = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

m2 = []
for i in range(3):
    m2.append([0, 0, 0])

for i in range(3):
    for j in range(3):
        m2[j][i] = m1[i][j]

# print('m1: ', m1)
print('m2: ', m2)

s=[sum(i) for i in m2]
print (s)