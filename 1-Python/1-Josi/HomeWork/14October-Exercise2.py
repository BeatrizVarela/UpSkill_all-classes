# -*- coding: utf-8 -*-
# """
# Created on Thu Oct 15 13:46:29 2020

# @author: Ana Beatriz Varela
# """

# ************************

# exercise 2 October 14th

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
w = 'Wrong input. Please, try again!'
user_answer = input("Welcome to A Padaria Portuguesa. Would you like to see the menu? (yes/no): ")
if user_answer == "yes":
    print('1 - Pão Alentejano')
    print('2 - Bolo Lêvedo [dos Açores]')
    print('3 - Bolo do Caco [da Ilha da Madeira]')
    print('4 - Broa')
    user_answer2 = input("Decided what to order? Tell us the number!: ")
    if user_answer2 == "1":
        print('Pão Alentejano')
    elif user_answer2 == "2":
        print('Bolo Lêvedo [dos Açores]')
    elif user_answer2 == "3":
        print('Bolo do Caco [da Ilha da Madeira]')
    elif user_answer2 == "4":
        print('Broa')
    else :
        print(w)
    user_answer3 = input("Would that be all? (yes/no): ")
    if user_answer3 == "yes":
        print(c)
    a = True
    while a :
        if user_answer3 == "no":
            user_answer2 = input("Decided what to order? Tell us the number!: ")
            if user_answer2 == "1":
                print('Pão Alentejano')
            elif user_answer2 == "2":
                print('Bolo Lêvedo [dos Açores]')
            elif user_answer2 == "3":
                print('Bolo do Caco [da Ilha da Madeira]')
            elif user_answer2 == "4":
                print('Broa')
            else :
                print(w)
            user_answer3 = input("Would that be all? (yes/no): ")
            if user_answer3 == "yes":
                print(c)
            else :
                print(w)
if user_answer == "no":
    print(c)
else :
    print(w)