# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:13:09 2020

@author: Ana Beatriz Varela
"""

#************************
# exercise 1
# ***********************

# input = [(1, 2, 3), (4, 5, 6)]
# output = [(1, 2, 9), (4, 5, 9)]

a = [(1, 2, 3), (4, 5, 6)]
new_list = []

for i in a:
    l = list(i)
    new_list.append(l)
# print(new_list)
for i in new_list:
    # print(i[2])
    i.remove(i[2])
    i.append(9)
# print(new_list)
f = []
# f = a.copy()
for i in new_list:
    f.append(tuple(i))
a = f
print(a)                # a = [(1, 2, 9), (4, 5, 9)]

#************************
# exercise 2
# ***********************

# my_obj = enumerate(['Cenas', 'What'])
    
# for i, j in my_obj :
#     print('i is: ', i)
#     print('j is: ', j)
    
my_obj = {1: 'one', 2: 'two'}
    
for i, j in my_obj.items() :
    print('i is: ', i)
    print('j is: ', j)

# Another solution
my_obj = [(1, 2), (3, 4), [5, 6]]
    
for i, j in my_obj :
    print('i is: ', i)
    print('j is: ', j)

#************************
# exercise 3
# ***********************

# input = [(1, 3), (2, 4) ('A', 8)]
# output = [(1, 2, 'A'), (3, 4, 8)]

# t = [(1, 3), (2, 4), ('A', 8)]
# new_list = []
# for z in t:
#     l = list(z)
#     new_list.append(l)
# # print(new_list)

# for a in new_list:
#     # print(a[1])
#     for b in new_list:
#         # print(b[1])
#         for c in new_list:
#             # print(c[1])
            
#             d1 = [(a[0], b[0], c[0]), (a[1], b[1], c[1]), (a[2], b[2], c[2])]
# print(d1)

a = [(1, 3), (2, 4), ('A', 8)]

A, B, C = a
new_list = []
for i in range(len(a)-1):
    D = [(A[i], B[i], C[i])]
    new_list.append(D)
print(new_list)

# ***********************