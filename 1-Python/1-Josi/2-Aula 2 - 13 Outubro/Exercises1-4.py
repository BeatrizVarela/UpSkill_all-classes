# -*- coding: utf-8 -*-

# Beatriz Varela

# ************************

# username Ana Beatriz Varela
# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/

# exercise 1

# ************************

# Try the following mathematical calculations and guess what is happening:
    # Suggestion: check the Python library reference at http://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

print((3 / 2))      #resultado da divisão
print((3 // 2))     #resultado da divisão para baixo
print ((3 % 2))     #resto da divisão
print((3**2))       #3 elevado a 2

# ************************

# exercise 2

# ************************

# Calculate the average of the following sequences of numbers:

print(2,4)          #6,8
print(4,8,9)        #13,17,18
print(12,14/6,15)   #27,29/6,30

# ************************

# exercise 3

# ************************

# The volume of a sphere is given by (4/3 * pi * r^3). Calculate the volume of a sphere of radius 5.
    # Suggestion: create a variable named "pi" with the value of 3.1415

# 1
pi = 3.1415
r = 5
v = (4/3*pi*(r**3))

print(f'{v:.3f} U')

# 2
pi = 3.1415
r = 5

print(f'{4/3*pi*(r**3):.3f} U')

# 3
pi = 3.1415
r = float(input('Enter sphere radius, please: '))
const = 4/3
power = 3
v = (const*pi*(r**power))

print(f'{v:.3f} U')

# ************************

# exercise 4

# ************************

# Use the modulo operator (%) to check which of the following numbers is even or odd:(1, 5, 20, 60/7).
    # Suggestion: the remainder of (x/2) is always zero when (x) is even.

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

# ************************