# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 08:34:53 2020

@author: Ana Beatriz Varela
"""

#************************

#Tuples

a = (1, 2, 3)

for i in a:
    i = a[0]
    i = a[1]
    i = a[2]

if i in a:
    i == a[0]
    i == a[1]
    i == a[2]
        
if i in a:
    if (i == a[0] or i == a[1] or i == a[2]):
        print('True')

#************************
# exercise 1
# ***********************
#Convert tuple into list and back again to tuple

t = (4, 6)          # t is a tuple
print(t)
a = list(t)         # t is a list now
print(a)

a.extend([9])       # add 9 to the list / also works with append = a.append(9)
print(a)

t = tuple(a)        # t is a tuple again
print(t)

#************************
# exercise 2
# ***********************
# Output: t = 'Python Course'

t = "$ $ Python$#Course  $"
t = t.strip('#$ ')
print(t)

t = t.replace('$#', ' ')
print(t)


t = "$ $ Python$#Course  $"
t = t.strip('#$ ')
a = list(t)
b = a.copy()

for i in a:
    if i == '#' or i == '$':        # i in ['#', '$']
        b.remove(i)
C = b.index('C')
b.insert(C, ' ')                    # b.insert(b.index('C'), ' ')

t = ''.join(b)
print(t)

# ***********************

t = (4, 8)
a, b = t
print(a)
print(b)

car = ('blue', 'auto', 7)
color, _, a = car
print(color)
print(_)
print(a)

#************************
# exercise 3
# ***********************
# Try Zip with 3 input variables

a = [1, 2, 'A']
b = ('Python', 161.8, 0, 5)
c = {10, 12, 14, 16, 18, 20}

print(list(zip(a, b, c)))           # [(1, 'Python', 10), (2, 161.8, 12), ('A', 0, 14)]

# Solution without zip
# Solution 1

c = list(c)                         # c is a set. convert to list to proceed
d1 = [(a[0], b[0], c[0]), (a[1], b[1], c[1]), (a[2], b[2], c[2])]
print(d1)

# Solution 2
i = 0
d2 = [(a[i], b[i], c[i]), 
      (a[i + 1], b[i + 1], c[i + 1]), 
      (a[i + 2], b[i + 2], c[i + 2])]
# d2 = [(a[i], b[i], c[i]), (a[i + 1], b[i + 1], c[i + 1]), (a[i + 2], b[i + 2], c[i + 2])]  SAME THING
print(d2)
# Solution 3

len(a)
len(b)
len(c)
min_abc = min(len(a), len(b), len(c))

e = []                              # e is list
for i in range(min_abc):
    (a[i], b[i], c[i])
    e.append((a[i], b[i], c[i]))

# Solution 4

len(a)
len(b)
len(c)
min_abc = min(len(a), len(b), len(c))

e = []                              # e is list
for i in range(min_abc):
    my_tuple = (a[i], b[i], c[i])
    e.append(my_tuple)

# ***********************

num = [8, 2, (9, 3), 4, (1, 6, 7), 34]
c = 0

for i in num:
    if isinstance(i, tuple):
        continue
    c += 1
print(c)
print(len(num) - c)                 # 2 (number of tuples)

#************************
# exercise 4
# ***********************
# How mny tuples are in num list?

num = [8, 2, (9, 3), 4, (1, 6, 7), 34]
c = 0

for i in num:
    if isinstance(i, tuple):
        continue
    c += 1
print(c)
print(len(num) - c)                 # 2 (number of tuples)  

# Solve it without isinstance

num = [8, 2, (9, 3), 4, (1, 6, 7), 34]
c = 0

for i in num:
    if type(i) == tuple:
        c += 1
print("There are", c, "tuples in num")

# ***********************