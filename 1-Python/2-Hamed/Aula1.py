# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 08:50:48 2020

@author: Ana Beatriz Varela
"""

a  = 3+2j               #Type: complex
print(a)

b = {'X':13}            #Type: dictionary
print(b)

c = 1 > 0               #Type: boolean
print(c)

d = 1 < 0               #Type: boolean
print(d)

e = {'X'}               #Type: set
print(e)

f = (3, -1, 'Python')   #Type: tuple
print(f)

#*****************

g = 1
h = 2
print(g + h)            #3 (Type: integer)

g = '1'
h = '2'
print(g + h)            #12 (Type: string)

i = 23
i << 1                  #46 (duplica cada um dos numeros)

i >> 1                  #11 (divide cada um dos numeros)       

#*****************

import math
n = -16
n = int(input('enter: '))
if n < 0 :
    n = abs(n)

print(math.sqrt(n))

#*****************

a = 5
if True :
    a = 6
print(a)

a = 20
if a % 2 == 0:
    print('even')
else:
    print('odd')

#*****************

x = 3
y = 2
if x == 1 or y == 1:
    print('ok')
else:
    print('no')

#*****************

names = ['sara', 'taha', 'farshid']
if 'ali' in names:
    print('found')
else:
    print('not found')

#*****************

a = 2
b = 5

if a < b:
    m = a
else: 
    m = b

m = a if a < b else b

#*****************

my_list = ['a', 'b', 'c']

if 'o' in my_list:
    s = 'yes'
else:
    s = 'no'

s = 'yes' if ('o' in my_list) else 'no'
print(s)

#*****************

score = 75

if score >= 90 :
    a = 'A'
elif score >= 80:
    a = 'B'
elif score >= 70:
    a = 'C'
else:
    a = 'D'
    
print(a)

#*****************

list(range(2, 10, 1))

#*****************

for j in range(5, 10, 2):
    print(j)

for j in range(5, 10, 2):
    print(j, end = '')
    
for j in range(5, 10, 2):
    print(j, end = ' ')

#*****************

#Print each character in one paragraph
s = 'Python'
for ch in s:
    print(ch)

#Print the number of characters in a word
word = 'python'

c = 0
for i in word:
    c += 1
print(c)

#*****************

#Print 'hello' 3 times
for _ in range(3) :
    print('hello')

#Print number of 'a' in a word
word = 'alireza'
c = 0
for i in word:
    if i == 'a':
        c += 1
print(c)

#Print vowels in a word
name = 'farshid'
v = 'aeiou'
c = 0
for ch in name:
    if ch in v:
        print(ch)
        c += 1
print(c)            #Prints the number of vowels

#Print vowels in a word
name = 'farshid'
v = 'aeiou'
a = [ch for ch in name if ch in v]
print(a)

#*****************

for i in range(1, 4):
    for j in range(2, 4):
        print(j, end = ' ')
    print()

#*****************

#Break
for i in range(5):
    if i == 3 :
        break
    else:
        print(i, end = ' ')

#Continue
for i in range(5):
    if i == 3 :
        continue
    else:
        print(i, end = ' ')

#*****************

#While eamples
i = 1
while i <= 3:
    print(i, end = ' ')
    i += 1

n = 7
while n >= 3:
    print(n, end = ' ')
    n -= 1

#While break/continue
#Break
s = 'abcdef'
i = 0
while True:
    if s[i] == 'd' :
        break
    print(s[i], end = ' ')
    i += 1

#Continue
n = 8
while n > 2:
    n -= 1
    if n == 5:
        continue
    print(n, end = ' ')

#*****************

#Game
import random
n = random.randrange(0, 10)
f = 'no'

print(n)

while f == 'no':
    a = int(input('Game: guess number between 0 to 9: '))
    if a < n :
        print('increase')
    elif a > n:
        print('decrease')












