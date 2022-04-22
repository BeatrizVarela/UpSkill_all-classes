# -*- coding: utf-8 -*-

# Beatriz Varela

# ************************

# username Ana Beatriz Varela
# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/

# Aula 3

# ************************

print(4==5)                 #False
print(5==5)                 #True
print(6>7)                  #False
print(15<100)               #True

print('hello' == 'hello')   #True
print('hello' == 'Hello')   #False

print('dog' != 'cat')       #True
print( True == True)        #False
print(True != False)        #True

print( 42 == 42.0)          #True (42 int 42.0 float)
print( 42 == '42')          #False (42 int '42' string)

print('apple' == 'Apple') 
# print('A unicode is', ord('A'),', a unicode is, ord('a'))            #!!!REVIEW!!!
print('apple' > 'Apple') 


minimum_age = 18
age = 14
if age > minimum_age:
    print('Congrats, you can get your license!')
else :
    print('Please, come back in {0} years.' .format(minimum_age - age)) 

minimum_age = 18
age = 70
if age > minimum_age:
    print('Congrats, you can get your license!')
else :
    print('Please, come back in {0} years.' .format(minimum_age - age)) 

# name =                                                                  #!!!TRY INPUT!!!
# password =
# if name == ‘Josi’:
#    print('Hello Josi')
# if password == 'swordfish':
#    print('Access granted.')
# else:
#    print('Wrong password.')

minimum_age = 18
user_age = 150
if user_age < minimum_age:
    print('Please, come back in {0} years.' .format(minimum_age - user_age)) 
elif user_age == 150 :
    print('Probably, you can not drive anymore. Please, make an appointment with your doctor.')
else :
    print('Congrats, you can get your license.')    

# ************************

# exercise 1

# ************************

# Write a code that guess the number stored in a variable   
# Input: guess_number  
# Expected Output:
# Please, guess higher  # if the guess_number is smaller than answer
# Please, guess lower   # if the guess_number is higher than answer 
# Congrats, you found the answer!!  

number = 5
user_number = int(input('Enter a number: '))
if user_number < number:                            #IF é sempre a primeira operação
    print('Please, guess higher.')
elif user_number == number :                        #Posso mudar a ordem das operações desde que faça sentido na lógica
    print('Congrats, you found the answer!!')
elif user_number == 9 : 
    print("No, it's not 9")
else :
    print('Please, guess lower.')   

# Comparisons using print 
# boolean

print((4 < 5) and (5 < 6))                                  #True
print((4 < 5) and (9 < 6))                                  #False
print((1 == 2) or (2 == 2))                                 #True
print(2 + 2 == 4 and not 2 + 2 == 5)                        #True
print((2 + 2 == 4 and not 2 + 2 == 5) and 2 * 2 == 2 + 2)   #True

# ************************

# exercise 2

# ************************

# a. Write a code to ask  How old are you? Store the age in a variable and print it 
# Expected input:  <Your age>
# Expected output <Your age>

age = int(input('How old are you? '))
print(age)

# b. Improve your code to check if you have age to retire or not
# Expected input:  <Your age>
# Expected output:   Have a good day at work     # if your age is in the range of 16 – 65
#  	   	You are too young to work, come back to school  # if <your age> smaller than 16
# 		You have worked enough, Let’s Travel now   # if <your age> greater than 65 

minimum_age = 18
max_age = 65
age = int(input('How old are you? '))
if age <= minimum_age :
    print('You are too young to work, come back to school.')
elif age > minimum_age and age < max_age :
    print('Have a good day at work')
else :
    print('You have worked enough, let’s travel now.')

# ************************

# Aula 3

# ************************

n = 5
while n > 0 :
    print(n)
    n = n - 1
print('Boom!!')
print(n)

n = 5
while n > 0 :
    print('Time')
    print('ticking')
print('Stopped')

while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')

while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')

# ************************




















