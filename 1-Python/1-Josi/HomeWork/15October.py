# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 20:31:21 2020

@author: Ana Beatriz Varela
"""

# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/

# ************************
# exercise 1
# ************************

# What do the following expressions evaluate to?

(5 > 4) and (3 == 5)                    # False
not (5 > 4)                             # False
(5 > 4) or (3 == 5)                     # True
not ((5 > 4) or (3 == 5))               # False
(True and True) and (True == False)     # False
(not False) or (not True)               # True

# ************************
# exercise 2
# ************************

# Identify the three blocks in this code:

spam = 0
if spam == 10:
      print('eggs')
      if spam > 5:
           print('bacon')
      else:
          print('ham')
      print('spam')
print('spam')

# inside the if statement
# and the lines print('bacon') and print('ham')

print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
print('spam')

# ************************
# exercise 3
# ************************

# Write a code that reads n numbers and print how many of them are in the following ranges:
# [0; 25], [26; 50], [51; 75] and [76; 100].
# For example, for n = 10 and the following numbers {2; 61; -1; 0; 88; 55; 3; 121; 25; 75} ,
# your program should print:

# 1 [0 ,25]: 4
# 2 [26 ,50]: 0
# 3 [51 ,75]: 3
# 4 [76 ,100]: 1

# def count_(list1, min, max):
# 	var = 0
# 	for var1 in list1:
# 		if min <= var1 <= max:
# 			var += 1
# 	return var

list1 = [2, 61, -1, 0, 88, 55, 3, 121, 25, 75]
a = '1 [0, 25]: '
b = '2 [26, 50]: '
c = '3 [51, 75]: '
d = '4 [76, 100]: '

v = 0
v1 = 0
v2 = 0
v3 = 0

for i in list1:
    if i in range(0, 26):
        v += 1
    elif i in range(26, 51):
        v1 += 1
    elif i in range(51, 76): 
        v2 += 1
    elif i in range(76, 101): 
        v3 += 1
print(a, v)
print(b, v1)
print(c, v2)
print(d, v3)

    # elif x in range(26, 51):
    #     print(b, (count_(list1, 26, 50)))
    #     break
    # elif x in range(51, 76):   
    #     print(c, (count_(list1, 51, 75)))
    #     break
    # elif x in range(76, 101):
    #     print(d, (count_(list1, 76, 100)))
    #     break


# a_list = [2, 61, -1, 0, 88, 55, 3, 121, 25, 75]
# x = int()

# for y in a_list:
#     if x >= 0 and x <= 25:
#         x = a_list.count(a_list)
#         print(x)
#         break
#     elif x >= 26 and x <=50:
#         y = y + 1
#     elif x >= 51 and x <=75:
#         y = y + 1
#     elif x >= 76 and x <=100:
#         y = y + 1

# n = int()
# list = [2, 61, -1, 0, 88, 55, 3, 121, 25, 75]
# if n in list in range(0, 25):
#     n = n + 1
#     print(n)

# list = [2, 61, -1, 0, 88, 55, 3, 121, 25, 75]
# a = range(0, 25)
# b = range(26, 50)
# c = range(51, 75)
# d = range(76, 100)
# for n in list:
#     for m in a:
#         if list[n] == a[m]:
#             break
#         print(list[m])
        

# ************************
# exercise 4
# ************************

# Use 10 strings methods of your choose to get information from this piece of text 
# Catching up
# Start with The Portuguese: The Land and Its People (3) by Marion Kaplan (Penguin), a one-volume introduction ranging from geography and history to wine and poetry, and Portugal: A Companion History (4) by José H Saraiva (Carcanet Press), a bestselling writer and popular broadcaster in his own country.

text = 'Catching up Start with The Portuguese: The Land and Its People (3) by Marion Kaplan (Penguin), a one-volume introduction ranging from geography and history to wine and poetry, and Portugal: A Companion History (4) by José H Saraiva (Carcanet Press), a bestselling writer and popular broadcaster in his own country.'
print(text.isnumeric())
print(text.istitle())
print(text.islower())
print(text.isupper())
print(text.lower())
print(text.upper())
print(text.split())
print(text.replace('p', 'f'))
print(text.isprintable())
print(text.isdecimal())

# ************************
# exercise 5
# ************************

# Write a code that reads a number (0-16) in the decimal base and prints that number in the binary base.

a = int(input('Enter a number to convert into binary: '))
print('The binary equivalent is:', bin(a))

# ************************