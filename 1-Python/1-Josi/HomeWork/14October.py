# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:37:46 2020

@author: Ana Beatriz Varela
"""

# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/

# ************************
# exercise 1
# ************************

# Write a code that reads two numbers and then a character that represents an
# arithmetic operator (‘+’, ‘-’, ‘*’ or ‘/’). Your program should then print the result
# operator applied to the two numbers given.

# sum
x = input("Type a number: ")
y = input("Type another number: ")
  
sum = int(x) + int(y)
  
print("The sum of {0} and {1} is {2}".format(x, y, sum)) 

# subtraction
x = input("Type a number: ")
y = input("Type another number: ")
  
sum = int(x) - int(y)
  
print("The subtraction of {0} and {1} is {2}".format(x, y, sum)) 

# multiplication
x = input("Type a number: ")
y = input("Type another number: ")
  
sum = int(x) * int(y)
  
print("The multiplication of {0} and {1} is {2}".format(x, y, sum)) 

# division
x = input("Type a number: ")
y = input("Type another number: ")
  
sum = int(int(x) / int(y))
  
print("The multiplication of {0} and {1} is {2}".format(x, y, sum)) 

# ************************
# exercise 2
# ************************

# Consider the following menu:

# 1 - Pão Alentejano
# 2 - Bolo Lêvedo [dos Açores]
# 3 - Bolo do Caco [da Ilha da Madeira]
# 4 - Broa
# 5 – I want to leave 

# Your program should:
# •	print the menu; 
# •	read a number from 1 to 5;
# •	and print the option menu corresponding to the number read. 
# This must be repeated until the user selects the option 5.

c = 'Come again!'
user_answer = input("Welcome to A Padaria Portuguesa. Would you like to see the menu? (yes/no): ")
if user_answer == "yes":
    print('1 - Pão Alentejano')
    print('2 - Bolo Lêvedo [dos Açores]')
    print('3 - Bolo do Caco [da Ilha da Madeira]')
    print('4 - Broa')
    print('5 - I want to leave')
    user_answer2 = input("Decided what to order? Tell us the number!: ")
    if user_answer2 == "1":
        print('Pão Alentejano')
    if user_answer2 == "2":
        print('Bolo Lêvedo [dos Açores]')
    if user_answer2 == "3":
        print('Bolo do Caco [da Ilha da Madeira]')
    if user_answer2 == "4":
        print('Broa')
    if user_answer2 == "5":
        print('I want to leave')
    user_answer3 = input("Would that be all? (yes/no): ")
    if user_answer3 == "yes":
        print(c)
    if user_answer3 == "no":
        print(user_answer2())
elif user_answer == "no":
    print(c)
   
# ************************
# exercise 3
# ************************
  
# What will be printed by the program below?
# Assume that the value of D in the ord(<letter>) of the first letter of your name.
# Example: ord(A) = 65
    
x = 5 + ord('B')                # x = 71
y = 0                           # y = 0
while True :
    y = (x % 2) + 10 * y        # y = 1             # y = 1
    x = x // 2                  # x = 35            # x = 0
    print ('x =', x, 'y =', y)  # x = 35 y = 1      # x = 0 y = 1
    if x == 0:
        break                                       # --Return--
    while y != 0:
        x = y % 100             # x = 1
        y = y // 10             # y = 0
    print ('x =', x, 'y =', y)  # x = 1 y = 0
      
# ************************
# exercise 4
# ************************
  
# Write a program that reads a positive integer n and prints n lines with the following
# format (example for n = 5 => 5 spaces) 
# 1 
#  2 
#   3
#    4
#     5

n = 1
print(' ' * n , n)
while n < 5 :
    n = n + 1
    print(' ' * n , n)

# ************************