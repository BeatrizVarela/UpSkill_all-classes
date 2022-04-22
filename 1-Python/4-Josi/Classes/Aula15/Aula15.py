# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 08:52:01 2020

@author: Ana Beatriz Varela
"""

# repository url: https://bitbucket.org/BeatrizVarela/python-code/src/master/

# ************************
# Aula 15
# ************************

'''
REVISIONS WEEK 1
'''
'''
List 2 - Exercise 1
1 - Write a code that reads two numbers and then a character that represents a
arithmetic operator (‘+’, ‘-’, ‘*’ or ‘/’). Your program should then print the result
operator applied to the two numbers given.
'''
# Expected exercise

firstNum = int(input("Tell me the first number:"))
# read second number
secondNum = int(input("Tell me the second number:"))

# boolean to control the loop
validOperation = False
# make operation using the variables with the values that were given
while not validOperation:
# read operator
    operator = input("Tell me which operator, out of the    following:\n '+', '-', '*' or '/'\n")
    if operator == "+":
        result = firstNum + secondNum
        validOperation = True
        break
    elif operator == "-":
        result = firstNum - secondNum
        validOperation = True
        break
    elif operator == "*":
        result = firstNum * secondNum
        validOperation = True
        break
    elif operator == "/":
        result = firstNum / secondNum
        validOperation = True
        break
    else:
        print("Value needs ot be one of the following operators    instead:\n '+', '-', '*' or '/' ")
        continue

# print result
print("The result of your operation is:", result, '\n')  


# Another solution

n1 = input('\nEnter first number: ')
n2 = input('\nEnter second number: ')
c = input('\nEnter the operator: ')

str = n1+c+n2
print(str)
print = (f'\n{n1} {c} {n2}')

res = eval(str)
print(type(res))
print("\nRES : ", res)

# ************************
'''
List 3 - Exercise 3
3 -Write a code that reads n numbers and print how many of them are in the following ranges: [0; 25], [26; 50], [51; 75] and [76; 100]. For example, for n = 10 and the following numbers {2; 61; -1; 0; 88; 55; 3; 121; 25; 75} , your program should print:
1 [0 ,25]: 4
2 [26 ,50]: 0
3 [51 ,75]: 3
4 [76 ,100]: 1
'''

# Expected exercise

print('\nExemplo 3: ')

r1 = 0
r2 = 0
r3 = 0
r4 = 0
for i in [2, 61, -1, 0, 88, 55, 3, 121, 25, 75]:
    if i in range(0, 26):
        r1 += 1
    if i in range(26, 51):
        r2 += 1
    if i in range(51, 76):
        r3 += 1
    if i in range(76, 101):
        r4 += 1

print("\n1 [0, 25]: ", r1)
print("2 [26, 50]: ", r2)
print("3 [51, 75]: ", r3)
print("4 [76, 100]: ", r4)

# ************************
'''
Guess Game
'''

guess_number = 5
user_number = True
while user_number:
    user_number = int(input("Enter a Number: "))
    if user_number < guess_number:                           
        print('Please, guess higher.')
    elif user_number == guess_number :                        
        print('Congrats, you found the answer!!')
        break
    elif user_number == 9 : 
        print("No, it's not 9")
    else :
        print('Please, guess lower.')   

# ************************
'''
Conditionals
'''

day = "Saturday"
temperature = 30
raining = True

if day == "Saturday" and temperature > 20 or not raining :
    print("Go out")
else :
    print("Better finishing python programming exercises")

'''
END OF REVISIONS WEEK 1
'''
# ************************

'''
REVISIONS WEEKS 2 AND 3
'''
'''
Importing modules
Finding functions attributes
Documentation

Lists:  <identification> =  [<value1>, <value2>] 
         Accepts different variable types 
         Index to access and/or find members
         Cannot change strings in lists using indexes 
         Ordered 
         usually for loop is used to manipulate lists
         It is possible to make slicing
         it is possible to concatenate lists with * and +
         in and in not indicates membership 
         it is possible to include a list inside other list
         Lists have methods such as .pop(), insert(), 
         count(), append()
         Filtering         
'''

# How does the import work:
import sqilte3
from sqlite import Error
from numpy import *
import numpy as np

b = [4, 6, 7]
print(np.add(b,5))

# The dir() method tries to return a list of valid attributes of the object.
print(dir(np))

# Example of a list
L = [3, True, "ali", 2.7, [5,8]]

a = [3, [109, 27], 4, 15]
print(a(1))             # TypeError: 'list' object is not callable
print(a[1])             # [109, 27]

a = []                  # Empty list
for i in range(4):
    a.append(i)         # This puts the range in the empty list
print(a)                # [0, 1, 2, 3]

# Counts only how many times 3 is included in the list
a = [1, 3, 6, 5, 3]
print(a.count(3))       # 2 

# ************************
'''
Tuples:  <identification> =  (<value1>, <value2>)
        Index to access and/or find members
        Cannot change strings in tuples using indexes 
        it is possible to concatenate lists with * and +
        Ordered 
it is possible to use python build in functions to manipulate tuples 
 Lists have methods such as .count(), .index(),
Removing member is only possible by converting to another type
It is possible to save tuple member in other variables - unpacking
A look in zip(),  
'''

# Index
t = ("English", "History", "Mathematics")
print(t[1])                 # History
print(t.index("English"))   # 0

# Count/Max/Concatenate
t = (1, 9, 3, 9)
print(t.count(9))           # 2
print(max(t))               # 9
print(t + t)                # (1, 9, 3, 9, 1, 9, 3, 9)

# Booleans
print((1, 2) == (2, 1))     # False

# Tuple > List > Remove > Tuple
t = (4, 7, 2, 9, 8)
x = list(t)
x.remove(2)
t = tuple(x)
print(t)                    # (4, 7, 9, 8)

a = (1, 2)
b = (3, 4)
c = zip(a, b)
x = list(c)
print(x)                    # [(1, 3), (2, 4)]
print(x[0])                 # (1, 3)

z = ((1, 3), (2, 4))
u = zip(*z)
print(list(u))              # [(1, 2), (3, 4)]

# ************************
'''
Dictionaries:  <identification> =  {<value1>: <value2>, 
                                  <value3>: <value4> }
Dictionaries have methods such as .get(), pop(), .popitem(), .copy(), .update()
It is possible to use python build in functions to manipulate     dictionaries  sum(). 
Sorting using operator module       
'''

# Replacing a value
d = {"brand": "cherry", "model": "arizo5", "color": "white"}
d["color"] = "black"
print(d)                    # {"brand": "cherry", "model": "arizo5", "color": "black"}

# Getting a key's value
x = d.get("model")
print(x)                    # arizo5

# Printing keys/values
print(list(d.keys()))       # ["brand", "model", "color"]
print(list(d.values()))     # ["cherry", "arizo5", "color"]

# Remove an item (key: value)
d.pop("model")
print(d)                    # {"brand": "cherry", "color": "black"}

# Turning two lists into one dictionary
k = ["red", "green"]
v = ["#FF0000", "#008000"]
z = zip(k, v)
d = dict(z)
print(d)                    # {"red": "#FF0000", "green": "#008000"}

# Sorting
num = {"ali": [12, 13, 8], "sara":[15, 7, 14], "taha": [5, 18, 13]}
d = {k : sorted(v) for k, v in num.items()}
print(d)                    # {"ali": [8, 12, 13], "sara":[7, 14, 15], "taha": [5, 13, 18]}

# ************************
'''
Sets:  <identification> =  {<value1>, <value2>,<value3>}
      Add values in the dictionary 
      Lists have methods such as .add(), update(), .remove(), .copy(), .update()
      joint theory 
      Subset 
'''

# Adding one item
f = {"apple", "orange", "banana"}
f.add("cherry")
print(f)                    # {"apple", "orange", "banana", "cherry"}

# Adding more than one item
f.update(["mango", "grapes"])
print(f)                    # {"apple", "orange", "mango", "banana", "grapes", "cherry"}

# Removing an item
f.remove("apple")
print(f)                    # {orange", "mango", "banana", "grapes", "cherry"}

# Union/Intersection
x = {1, 2, 3}
y = {2, 3, 4}
print(x.union(y))           # {1, 2, 3, 4}
print(x | y)                # {1, 2, 3, 4}

print(x.intersection(y))    # {2, 3}
print(x & y)                # {2, 3}

# Subset
a = {1, 2, 4}
b = {1, 2, 3, 4, 5}
print(a.issubset(b))        # True
print(b.issubset(a))        # False

# ************************
'''
Files:
         Open files  open(), .close() 
open(<path to the file>, <Mode>)
With open takes care of closing files 
'''

epopeia = open ("C:\\Users\\User\\python-code\\4-Josi\\Classes\\Aula15\\epopeia.txt", "r")

for line in epopeia:
    print(line)
    if "tempestade" in line.lower():
        print(line)

epopeia.close()

with open ("C:\\Users\\User\\python-code\\4-Josi\\Classes\\Aula15\\epopeia.txt", "r") as epopeia:
    for line in epopeia:
        if "tempestade" in line.lower():
            print(line)
print(line)                 # Printa a última linha do documento

# ************************

# encoding_type = "utf-8"             
file_path = ("C:\\Users\\User\\python-code\\4-Josi\\Classes\\Aula15\\epopeia.txt")
epopeia = open (file_path, "r", encoding="utf-8") # ou encoding = encoding_type          # Encoding para ler os acentos   

for line in epopeia:
    print(line)
    if "tempestade" in line.lower():
        print(line)

epopeia.close()

# ************************
'''
Files:
         manipulating files .read(), .readline() .readlines() 
         readline() – Reads a single line of the file and return a string
         readlines() – reads the entire file and return a list of strings 
         read () – reads the entire file and return a string 
'''

file_path = ("C:\\Users\\User\\python-code\\4-Josi\\Classes\\Aula15\\epopeia.txt")

with open (file_path, "r", encoding="utf-8") as epopeia:
    line = epopeia.readline()       # Só imprime uma linha (sem o loop while!)
    while line:
        print(line, end="")
        line = epopeia.readline()

# ************************

file_path = ("C:\\Users\\User\\python-code\\4-Josi\\Classes\\Aula15\\epopeia.txt")

with open (file_path, "r", encoding="utf-8") as epopeia:
    poem = epopeia.readlines()      # Lista
    print(type(poem))
print(poem)

# ************************

file_path = ("C:\\Users\\User\\python-code\\4-Josi\\Classes\\Aula15\\epopeia.txt")

with open (file_path, "r", encoding="utf-8") as epopeia:
    text = epopeia.read()           # String gigante
    print(type(text))
print(text)

# ************************

for linea in poem[::-1] :
    print(linea, end="")
print(type(poem))                   # List

for linea in text[::-1] :
    print(linea, end="")
print(type(text))                   # String

# ************************
'''
Files:
         Json files – JavaScript Object Notation file – easy to understand by human and machines 
         Data is separated by commas.
         Curly braces hold objects.
         Square brackets hold array 
         
         HOW TO CREAT A JSON FILE:
             - WRITE THE JSON CODE IN THE NOTEPAD AND SAVE IT AS *.json

To validate JSON code: https://jsonlint.com/?code=

{
 "data": [
{
             "id": "12341 ",
             "name": "Joseanne Viana",
             "address":  {
                 "city": "Lisboa"
                 "state ": "Lisboa ",
                 "postal_code": "1000569"
                 },
            "position ": "PhD Student"
                 } 
     ]
 }
'''

# ************************
'''
Files:
         Json files – import json packet 
         open (<path to the file >)  json.load(<object>), 
         json.dumps(<pythonObject>, <formatting attribute>) – convert python objects in json objects 
         json.dump((<pythonObject>, <fileObject>, <formatting attribute>) ) – write json files        
'''

import json

with open("C:\\Users\\User\\python-code\\4-Josi\\Classes\\Aula15\\dados.json") as json_file:
    jsonObject = json.load(json_file)
    name = jsonObject["data"][0]["name"]
    address = jsonObject["data"][0]["address"]["city"]
    
    print(jsonObject)
    print(name)
    print(address)
    
    a = json.dumps(jsonObject, indent = 4)
    print(a)

# ************************

import json

file_path = "C:\\Users\\User\\python-code\\4-Josi\\Classes\\Aula15\\dados2.json"
with open(file_path) as json_file:
    jsonObject = json.load(json_file)
    name = jsonObject["data"][0]["name"]                        # Nome da Joseanne
    address = jsonObject["data"][2]["address"]["postal_code"]   # Código postal da Rita
    
    # print(jsonObject)
    print(name)
    print(address)
    
    a = json.dumps(jsonObject, indent = 4)
    print(a)

# ************************
'''
Files: 
    Excel files 
	     Pandas packet is frequently used to manipulate excel files 
'''

import pandas as pd
a = "C:\\Users\\User\\python-code\\4-Josi\\Classes\\Aula15\\Employee_data.xlsx"
all_data = pd.read_excel(a, index_col = 1)

email = all_data["email"].head()
company_name = all_data["company_name"]
xl = pd.ExcelFile(a)
df = xl.parse("b")

# ************************