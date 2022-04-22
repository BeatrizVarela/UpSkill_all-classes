# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:19:00 2020

@author: Ana Beatriz Varela
"""

#************************
# October 26th
# ***********************

'''
Exercise 1
'''

d1 = {'a': 1, 'b': 3, 'c': 2}
d2 = {'a': 2, 'b': 3, 'c': 1}

d1.update(d2)
d1.pop("a")
d1.pop("c")
print(d1)


'''
Exercise 2
'''

while True:
    a=input("Insert a: ")
    b=input("Insert b: ")
    c=input("Insert c: ")
    d=input("Insert d: ")
    if a.isdigit()!=True or b.isdigit()!=True or c.isdigit()!=True or d.isdigit()!=True:
        print("Insert valid numbers.")
        continue
    elif a==b or c==d:
        print("Insert diferent numbers.")
        continue
    else:
        a=int(a)
        b=int(b)
        c=int(c)
        d=int(d)
        break
if a>b:
    a,b=b,a
elif c>d:
    c,d=d,c
else:
    pass
a_b=set(range(a,(b+1)))
c_d=set(range(c,d))
if a in (a_b&c_d) and not b in (a_b&c_d):
    print("There is an intersection between a and d, not counting d.")
elif a_b==(a_b&c_d):
    print("a to b is a part of c to d.")
elif b in (a_b&c_d) and not a in (a_b&c_d):
    print("There is an intersection from c to b.")
elif c_d==(a_b&c_d):
    print("c to d is a part of a to b.")
else:
    print("There is no intersection between a to b and c to d.")