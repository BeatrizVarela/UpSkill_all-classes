# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 08:41:55 2020

@author: Ana Beatriz Varela
"""

#************************

#Lists
a = [5, 7, 12]
print(a[0])
print(a[1])
print(a[2])

print(type(a))
print(len(a))

b = [1.618, 'Python Course', 0, {'joe':2}, [], (3, 6, 9)]
print(b)

dir(list)           # dir() tells what functions can be used with this type of variable (this case, a list)

#************************

a = [5, 7, 12]
print(a.index(7))

# 5 = 0
# 7 = 1
# 12 = 2

#List is mutable
a[1] = 8            # 7 = 8
print(a)

s = 'sara'
print(s[1])
s[1] = 'd'          # ERROR: You cannot change strings with this way

#List is Ordered
a = [1, 2]
b = [2, 1]
print(a == b)       # False

# Dictionary is ordered in the latest version
# Set is ordered
w = {1, 2}
print(w)

#************************

friends = ['Hamed', 'Josi', 'Stefan']
for f in friends:
    print(f)
    
friends = ['Hamed', 'Josi', 'Stefan']
for i in range(1) :   # range (len(friends))
    print(friends[i])

#************************

my_list = [1, 2, 23, 4, 'word']
for i in [0, 1, 2, 3, 4]:
    print(my_list[i], my_list[i + 1])   # ERROR: out of range

my_list = [1, 2, 23, 4, 'word']
for i in range((len(my_list))):
    print(my_list[i], my_list[i + 1])   # ERROR: out of range


#Solved
my_list = [1, 2, 23, 4, 'word']
for i in [0, 1, 2, 3, 4]:
    print(my_list[i], my_list[i + 1])
    if i == 3:                          # When I know list lenght
        break
    
my_list = [1, 2, 23, 4, 'word']
for i in [0, 1, 2, 3, 4]:
    if i == len(my_list) - 1:           # When I don't know list lenght
        break
    print(my_list[i], my_list[i + 1])
        
my_list = [1, 2, 23, 4, 'word']
for i in range(len(my_list)-1):         # When I don't know list lenght
    print(my_list[i], my_list[i + 1])

# 1 2
# 2 23
# 23 4
# 4 word

#************************

#Code wrongly written for explaining proposes
a = [7, 5, 30, 2, 6, 25]

list_name[Start:Stop]
print(a[1:4])                   # [5, 30, 2]

list_name[ :Stop]
':' means start from the first, step is +1
print(a[:3])                    # [7, 5, 30]

list_name[Start: ]
':' means until the end, step is +1
print(a[3:])                    # [2, 6, 25]

Start > Stop, No Step means 'Step = +1'
print(a[3:0])                   # []

Start > Stop, Step = -1
remember that the Stop is NOT included
print(a[3:0:-1])                # [2, 30, 5]

list_name[ : :-1]
reverse a list
print(a[::-1])                  # [26, 6, 2, 30, 5, 7]

#************************

a = [7, 5, 30, 2, 6, 25]
print(a)                        # [7, 5, 30, 2, 6, 25]
a[3:5]=[14, 15]
print(a)                        # [7, 5, 30, 14, 15, 25]

#************************

a = [4, 7]
b = a*2
print(b)

a = [1, 2]
b = ['a', 'b', 'c']
print(a + b)

a = [7, 5, 30, 2, 6, 25]
print(14 in a)                  # False
print(14 not in a)              # True

a = [3, [109, 27], 4, 15]
print(a[1])                     # [109, 27] (type: list)
print(a(1))                     # ERROR
print(a[1][1])                  # 27 (type: integer)
print(a[1, 1])                  # ERROR
print(len(a))                   # 4 (type: integer)

#************************
# Exercise 1
#************************

a = [7, 5, 30, 2, 6, 25]
m = a[0]
for i in a :
    if i > m:
        m = i
print(m)
print(max(a))
print(min(a))
print(a.index(m))

s = 0
for i in a :
    s += i
print(s)
print (sum(a))

#************************

a = [1, 2, 3]
print(a)                    # [1, 2, 3]
print(a[::-1])              # [3, 2, 1]
a.reverse()
print(a)                    # [3, 2, 1]

b = a.reverse()
print(b)                    # None

b = (a[::-1])
print(b)                    # [3, 2, 1]

#************************

x = ['Ana', 'Beatriz']
print(x)
x.extend(['Varela'])
print(x)

#************************

a = ['Python', 1, 2, 3]
b = [11, 14]

a.append(b)
print(a)                    # ['Python', 1, 2, 3, [11, 14]]

print(a[-1])                # [11, 14]
print(a[-1][0])             # 11
print(a[-1][-1])            # 14

#************************

a = []
for i in range(101):
    a.append(i)
print(a)

a = [1, 2, 3]
for i in range(11):
    a.append(i)
print(a)

#************************

a = [1, 2, 3]
c = a               # a, c are dependent

a[0] = 56

b= a.copy()         # a, b are independent
a[0] = 0
b[0] = 99

d = a[::]
e= a[:]
a[0] = 88

d[0] = 22

#************************

x = 2
y = x
y += 1
print(x)            # 2
print(y)            # 3
# X won't change because it's an integer, not a list

x = []
y = x
y.append(5)
print(x)            # [5]
print(y)            # [5]

#************************

a = [i for i in range(4)]
print(a)                        # [0, 1, 2, 3]

a = [i*2 for i in range(4)]
print(a)                        # [0, 2, 4, 6]

a = [i*i for i in range(3,6)]
print(a)                        # [9, 16, 25]

#************************

a = 'Bea4Tri$'
b = list(a)

#Use strip module
c = ''.join(b)

#************************
# Exercise 2
#************************

a = [1, 2]
b = [1, 4, 5]
c = []

for i in a:
    for j in b:
        if i != j:
            c.append((i,j))
print(c)

#************************

a = [2.6, float('NaN'), 4.8, 6.9, float('NaN')]
b = []

import math

for i in a :
    if not math.isnan(i):
        b.append(i)
print(b)

# If you want to change the lenght of a list, dict or set in a loop and want to remove/add some objects,
# you need to check the itterable variable in your loop. 
# If you used the same list/dict or set, you need to make a copy.

a = [1, 2, 3, 4]
for i in a :
    if i > 2:
        a.pop()
print(a)

a = [1, 2, 3, 4]
for i in a :
    if i < 2:
        a.pop()
print(a)

a = [1, 2, 3, 4]
for i in a :
    if i == 2:
        a.pop()
print(a)

#************************