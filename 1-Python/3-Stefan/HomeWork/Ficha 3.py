# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:05:26 2020

@author: Ana Beatriz Varela
"""

# ************************
# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/
# ************************

'''
Ficha 3
'''

'''
1. Qual o valor de cada expressão?
a. map(lambda x:x+1, range(1,4))
b. map(lambda x:x>0, [3,−5,−2,0])
c. filter(lambda x:x>5, range(1,7))
d. filter(lambda x:x%2==0, range(1,11))
'''

a = map(lambda x:x+1, range(1,4))           # (2, 3, 4)
b = map(lambda x:x>0, [3, −5, −2, 0])       # [3]
c = filter(lambda x:x>5, range(1,7))        # (6)
d = filter(lambda x:x%2==0, range(1,11))    # (2, 4, 6, 8, 10)


'''
2. Determine o valor de cada uma das expressões seguintes:
a. reduce(lambda y, z: y* 3+z, range(1,5))
b. reduce (lambda x, y: x** 2+y, range(2,6))
'''

a = reduce(lambda y, z: y* 3+z, range(1,5))     # 18
# y = 1
# z = 2
# t = y* 3+z
# y = 3
# z = 4
# u = y* 3+z
# v = t + u

b = reduce(lambda x, y: x** 2+y, range(2,6))   # 28
# x = 2
# y = 3
# t = x** 2+y
# x = 4
# y = 5
# u = x** 2+y
# v = t + u

# ************************