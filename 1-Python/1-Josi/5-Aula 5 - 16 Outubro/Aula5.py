# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 08:33:40 2020

@author: Ana Beatriz Varela
"""

# ************************

# Aula 5

# ************************

import math                                 #Importar funções

def volume_sphere(r, power, const):         #def = define o volume da esfera, como uma 'caixa preta'
    v = (const*math.pi*(r**power))          #Usar a função importada
    print(f'{v:.3f} U')
    
r = float(input('Enter sphere radius, please: '))
const = 4/3
power = 3
volume_sphere(r, power, const)

# ************************

def volume_sphere(r, power, const):         #def = define o volume da esfera, como uma 'caixa preta'
    v = (const*math.pi*(r**power))          #Usar a função importada
    return v
    
r = float(input('Enter sphere radius, please: '))
const = 4/3
power = 3
v = volume_sphere(r, power, const)
print(f'{v:.3f} U')

# ************************

def food(vegetable):
    if vegetable == 'tomato':
        print('I bought tomato')
    elif vegetable == 'orange':
        print('i bought orange')
    else:
        print('I bought other vegetable')

food('tomato')

# ************************

def addtwo(a, b):
    added = a + b
    minus = a - b
    return added, minus

x = addtwo(3, 5)
print(x)
print(x[0])
print(x[1])

# ************************

def food():
    eggs = 'food local'
    print(eggs)

def more_food():
    eggs = 'more_food local'
    print(eggs)
    food()
    print(eggs)

eggs = 'global'
more_food()
print(eggs)

# ************************

for i in [2, 61, -1, 0, 88, 55, 3, 121]:
    print(i)

# ************************

a = 21
b = 10
c = 0

c = a + b
c += a          # c + a
c *= a          # c * a
c /= a          # c / a float

c = 2

c %= a          # resto de c a dividr por a
c **= a         # c elevado a a
c //= a         # c / a int

# ************************

a = 10
b = 3

hifen = 30
binary = bin(a & b);
denary = a & b
print('Line 1 - Value of binary is ', binary)
print('Line 1 - Value of denary is ', denary)
print('-'*hifen)

binary = bin(a | b);
denary = a | b
print('Line 1 - Value of binary is ', binary)
print('Line 1 - Value of denary is ', denary)
print('-'*hifen)


# ************************

# Exercise 1

# ************************

# Implement a function that recieves a number as parameter and prints, in decreasing order, which
# numbers are even and which are odd, until it reaches 0.
# >>> even_odd(10)
# Even number: 10
# Odd number: 9
# Even number: 8
# Odd number: 7
# Even number: 6
# Odd number: 5
# Even number: 4
# Odd number: 3
# Even number: 2
# Odd number: 1

def even_odd(x):
    if x % 2 == 0:
        print("Even number: ", x)
    else :
        print("Odd number: ", x)
    # return()

x = int(input('Type a number from 0 to 10: '))
even_odd(x)
# y = range(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)




def even_odd(x):
    if x >= 0 and x <= 10:
        for i in range(x, 0, -1):
            if i % 2 == 0:
                print("Even number: ", i)
            else :
                print("Odd number: ", i)
    else :
        print('Number not valid!')
    

x = int(input('Type a number from 0 to 10: '))
even_odd(x)

