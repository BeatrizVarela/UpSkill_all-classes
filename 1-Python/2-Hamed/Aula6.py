# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 08:54:20 2020

@author: Ana Beatriz Varela
"""

#************************
# exercise 6
# ***********************

# find number of X occurences in S

# Input:
# s = 'Python Course'
# x = ['o', 'r']

# Output:
# {'o': 2, 'r': 1}

s = 'Python Course'
x = ['o', 'r']

d = {}

for i in s:
    if i in x:
        d[i] = d.get(i, 0) + 1

print(d)

#************************
# exercise 7
# ***********************

d = {'x': 3, 'y': 2, 'z': 1, 'y': 4, 'z': 2}

r = {}

for k, v in d.items():
    if k not in r.keys():
        r[k] = v

print(r)

#************************
# exercise 8
# ***********************
# How many 'Trues'?

students = [
            {'id': 123 , 'name': 'Sophia' , 's': True},
            {'id': 378 , 'name': 'William' , 's': False},
            {'id': 934 , 'name': 'Sara' , 's': True}
            ]

# print(True + True)      # 2
# print(True + False)     # 1
# print(True + 1)         # 2
# print(True + 3.14)      # 4.14

# a = students[0]
# b = students[1]
# c = students[2]
# a['s']

sum_True = 0
for i in students:
    # print(i['s'])
    sum_True += int(i['s'])         # int optional
print(sum_True)

# ***********************

a = []
b = ()
c = {}
d = set()

a2 = list()
b2 = tuple()
c2 = dict()

# ***********************

# Set is not ordered

f = {'apple', 'orange', 'banana'}
m = set (('orange', 'apple', 'banana'))
f == m          # True

# Set is not ordered

f.add('cherry')                     # Use with only one argument
print(f)

f.add(('watermelon', 'coconut'))    # Adds arguments as a tuple
print(f)

f.update(['mango', 'pear'])         # Use with more than one argument
print(f)

f.update('papaya')                  # Adds argument
print(f)

f.remove('cherry')                  # Removes argument
print(f)

# ***********************

vowels = {'a', 'e', 'i', 'o', 'u'}

vowels.remove('a')
vowels.discard('k')                 # If 'k' exists in vowels, remove. Else, No Error.

V2 = vowels                         # V2 and vowels are dependent

c = vowels.copy()
print(vowels)

x = vowels.pop()                    # randomly remove one of the members in set

print(x)                            # a
print(vowels)                       # {'u', 'o', 'i', 'e'}
print(V2)                           # {'u', 'o', 'i', 'e'}
print(c)                            # {'u', 'o', 'i', 'e', 'a'}

vowels.clear()

# ***********************
# Union | Intersection & Update

x = {1, 2, 3}
y = {2, 3, 4}
print(x.union(y))           # {1, 2, 3, 4}
print(x | y)                # {1, 2, 3, 4}

x = {1, 2, 3}
y = {2, 3, 4}
print(x.intersection(y))    # {2, 3}
print(x & y)                # {2, 3}

x = {1, 2, 3}
y = {2, 3, 4}
x.update(y)
print(x)                    # {1, 2, 3, 4}

# ***********************
# Difference | Difference_update | Symmetric_difference | ^

a = {1, 2, 3, 4, 5}
b = {2, 4, 7}
print(a - b)                # {1, 3, 5}
print(b - a)                # {7}

r = a.difference(b)
print(r)                    # {1, 3, 5}
print(a)                    # {1, 2, 3, 4, 5}
print(b)                    # {2, 4, 7}

x = {1, 2, 3}
y = {2, 3, 4}
print(x.symmetric_difference(y))        # {1, 4}
print(x ^ y)                            # {1, 4} ^ is XOR
print(x.union(y) - x.intersection(y))   # {1, 4}
print(x.union(y) - y.intersection(x))   # {1, 4}

r = a.difference_update(b)
print(r)                    # None
print(a)                    # {1, 3, 5}
print(b)                    # {2, 4, 7}

#************************
# exercise 1
# ***********************

a = {10, 4, 9, 1, 3, 6, 2}
b = {13, 4, 9, 1, 3, 15, 14}
c = {11, 12, 14, 15, 1, 9, 3, 2, 6}

print(c - (a & b))
# print(c - a.intersection(b).intersection(c))
print((a & b) - c)
# print(a & b - c)
print((a | b) - c)
# print(a.union(b) - c)

# ***********************

d = {'one': 1, 'two': 2}
print('one' in d)           # True
print(1 in d)               # False

x = {1, 2}
y = {1, 2, 3}
print(x.isdisjoint(y))      # False

x = {1, 2}
y = {3, 7, 8}
print(x.isdisjoint(y))      # True

a = {1, 2, 4}
b = {1, 2, 3, 4, 5}
print(a.issubset(b))        # True
print(b.issubset(a))        # False

c = set()
print(c.issubset(a))        # True
print(a.issubset(c))        # False

#************************
# exercise 2
# ***********************
# Which characters are in 'Python Course'?
# Output = 'o', 'y'

a = {'a', 'y', 'c', 'o', 'z'}
b = 'Python Course'

print(a.intersection(b))

#************************
# exercise 3 (HomeWork)
# ***********************
# Find match key:value in 2 dictionaries
# Try to use set()
# Output: {'b': 3}

d1 = {'a': 1, 'b': 3, 'c': 2}
d2 = {'a': 2, 'b': 3, 'c': 1}

a = d1.items()
b = d2.items()

for i in a:
    print(i)









