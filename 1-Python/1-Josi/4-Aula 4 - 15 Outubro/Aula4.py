# -*- coding: utf-8 -*-
# """
# Created on Thu Oct 15 08:49:57 2020

# @author: Ana Beatriz Varela
# """

# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/

# ************************

# Aula 4

# ************************

a = 10
b = a
c = 9
d = c
c = c + 1

print(a)
print(b)
print(c)
print(d)
print(c)
print('')

# ************************

# While

n = 5
while n > 0 :
    print(n)
    n = n - 1
print('Boom!!')
print(n)

# For

for i in [5, 4, 3, 2, 1] :
    print(i)
print('Bomm!!')

friends = ['Ana', 'Filipe', 'João']
for friend in friends :
    print('Congrats on your new job:', friend)
print('Done!')

# Range

print('Before')
for i in range(5):
    print(i)
print('After')

print('Before')
for i in range(2, 6):
    print(i)
print('After')

print('Before')
for i in range(15, 0, -5):
    print(i)
print('After')

# ************************

# Exercise 1

# ************************

# Write a code to print out the capital letters in a string
# The best of made in Portugal - Hats, Soaps, Shoes, Tiles & Ceramics, Corks
# Expected input: The Best of made in Portugal - Hats, Soaps, Shoes, Tiles & Ceramics, Corks
# Expected output:TBPHSSTCC

def only_upper(s):
    print(s)
    upper_chars = ""
    for char in s:
        if char.isupper():
            upper_chars += char
    return upper_chars

print(only_upper("The Best of made in Portugal - Hats, Soaps, Shoes, Tiles & Ceramics, Corks"))


def only_lower(s):
    print(s)
    lower_chars = ""
    for char in s:
        if char.islower():
            lower_chars += char
    return lower_chars

print(only_lower("The Best of made in Portugal - Hats, Soaps, Shoes, Tiles & Ceramics, Corks"))


# ************************

msg = "beatriz"
a = msg.capitalize()
print(a)

# ************************

msg = "Ana beatriz pereira varela"
b = msg.count('a')
c = msg.count('A')
d = b + c
print(d)

# ************************

# Exercise 2

# ************************

# Write a code to print numbers from 0 - 50 divisible by 4
# Consider 0 in your code
# Expected output:
# 0
# 4
# 8
# 12
# 16
# 20
# 24
# 28
# 32
# 36
# 40
# 44
# 48

for i in range(0, 50, 4):
    print(i)

# ************************

# Exercise 3

# ************************

largest = -1
print('Before', largest)
for num in [9, 41, 12, 3, 74, 15] :
    if num > largest :
        largest = num
    print(largest, num)
print('After', largest)


loop = 0
print('Before', loop )
for thing in [9, 41, 12, 3, 74, 15] :
    loop = loop
    print(loop , thing)
print('After', loop )

loop = 0
print('Before', loop )
for thing in [9, 41, 12, 3, 74, 15] :
    loop = loop + 1
    print(loop , thing)
print('After', loop )


sum = 0
print ('Before', sum)
for thing in [9, 41, 12, 3, 74, 15] :
    sum = sum + thing
print(sum, thing)




















