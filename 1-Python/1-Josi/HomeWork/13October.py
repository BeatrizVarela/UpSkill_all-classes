# -*- coding: utf-8 -*-

# Beatriz Varela

# ************************

# username Ana Beatriz Varela
# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/

# exercise 1

# ************************

# Answer what type of object(variable) should be used to store each of the following information:
# a. A person's age
# b. The area of your yard in square meters
# c. The amount of money in your bank account 
# d. The name of your favorite songs

age = 30
print(type(age))
area = 20
print(type(area))
money = 1000
print(type(money))
song = 'Sad Machine'
print(type(song))
singer = 'Porter Robinson'
print(type(singer))

print(f"I'm {age} years old and my yard is {area}m\u00b2. I also have \u20ac{money} in my bank account and my favorite song is {song} by {singer}.")

a = "I'm"
b = "years old and my yard is"
c = "m\u00b2. I also have \u20ac"
d = "in my bank account and my favorite song is"
e = "by"

print(f"{a} {age} {b} {area}{c}{money} {d} {song} {e} {singer}.") #simplified

# ************************

# exercise 2

# ************************

#Write a Python program that accepts a word from the user and reverse it

s = input("Enter a word: ")
print(s[::-1])
print('')

# ************************

# exercise 3

# ************************

# Initialize the string “abc” on a variable named “s”:
# a. Use a function to get the length of the string.
# b. Write the necessary sequence of operations to transform the string “abc” in “aaabbbccc”
    # Suggestion: Use string concatenation and string indexes.

s = 'abc'
print(len(s))

s = "abc"
s1 = str()                      # a new, empty string.
for char in s:
    s1 += char + char + char    # strings concatenate using + and +=
    s1                          # the duplicant string
print(s1)

print('')

# ************************

# exercise 4

# ************************

# Initialize the string “aaabbbccc” on a variable named “s”:
# a. Use a function that allows you to find the first occurrence of “b” in the string, and the first occurrence of “ccc”.
# b. Use a function that allows you to replace all occurrences of “a” to “X”, and then use the same function to change only the first occurrence of “a” to “X”.

s = 'aaabbbccc'
print(s.find('b'))
print(s.find('ccc'))

print(s.replace('a', 'X'))
s1 = s[0:1].replace('a', 'X') + s[1:9]
print(s1)
print('')

# ************************

# exercise 5

# ************************

# Starting from the string “aaa bbb ccc”, what sequences of operations do you need to arrive at the following strings? 
    # You can use the “replace” function.
    # 1. “AAA BBB CCC”
    # 2. “AAA bbb CCC

s = 'aaa bbb ccc'
print(s.upper())
s1 = s[0:3].upper() + s[3:7] + s[7:11].upper()
print(s1)
print('')

# ************************

# exercise 6

# ************************

# Consider the code below:
# a = 10
# b = a
# c = 9
# d = c
# c = c + 1
# After executing this code snippet, what will be the value stored in each variable?

a = 10
b = a
c = 9
d = c
c = c + 1

print(a)    #10
print(b)    #10
print(c)    #9
print(d)    #9
print(c)    #10

# ************************

# exercise 7

# ************************

# Write a code that reads two integer values in the variables x and y and change the content of the variables.
# For example, assuming that x = 2 and y = 10 were the values read, your program should make x = 10 and y = 2.
# Redo this problem using only x and y as variables.

x = 2
y = 10

print(x)                #x = 2
print(y)                #y = 10

x, y = y, x             #Assignment

print(x)                #x = 10
print(y)                #x = 2

# ************************

# exercise 8

# ************************

# Consider a program that should classify a number as odd or even and, in addition,
# classify it as less than 100 or greater than or equal to 100. The solution below does this
# classification correctly?

print (" Enter a number  :")
a = int(input())
if a % 2 == 0 and a < 100:
    print ("The number is even and smaller than 100")
elif a % 2 == 0 and a > 100:
    print ("The number is even and higher than 100")
else :
    if a == 100:
        print ("The number is even and equal to 100")
if a % 2 != 0 and a < 100:
        print ("The number is odd and smaller than 100")
else :
    if a % 2 != 0 and a > 100:
        print ("The number is odd and higher than 100")
        
# Odds and Evens
# print (" Enter a number  :")
# x = int ( input ())
# if x % 2:
#     print("Odd")
# else :
#     print("Even")

# ************************