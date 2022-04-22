# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 08:38:37 2020

@author: Ana Beatriz Varela
"""

#**************************
# Ficha 2 - Exercício 8
#**************************

b = 5655

def unidades (a): 
    a = str(a)
    if len(a) < 2:
        return 0
    else:
        return int(a[:-1])

print(unidades(b))

#**************************

# f = open('lorem-ipsum.txt', 'w')
# write - escreve info no ficheiro, mas apaga o conteudo original

# f = open('lorem-ipsum.txt', 'a')
# append - adiciona ao final do ficheiro sem apagar a info previa

# f = open('lorem-ipsum.txt', 'x')
# uma forma de cria um ficheiro e dá erro se o fich já existir

f = open('lorem-ipsum.txt', 'r')
# abre-se um ficheiro para leitura
# print (f.read())
# read_result = f.read(40)
# lê os primeiros 40 caracteres, e o espaço em branco conta como 1 ch
# read_result = f.readline() # lê uma linha
# print (read_result)
print (f.readline())

for line in f: # semelhante a fazer f.readline()
    print (line)

# no final do trabalho temos que fechar o ficheiro
f.close()


# with open('lorem-ipsum.txt') as file_reader:# forma para nao ter de escrever open e close
#     for line in file_reader: 
#         print (line)

print (f.closed) # dá para verificar se o ficheiro está aberto ou não

#**************************

# Open the file "demofile2.txt" and append content to the file:
f = open('lorem-ipsum.txt', "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open('lorem-ipsum.txt', "r")
print(f.read())

#**************************

'''
ERRORS
'''

int('abc')          # ValueError: invalid literal for int() with base 10: 'abc'

# The string must contain numbers, not letters
# Thanks
try:
    int('abc')
except ValueError:
    print('The string must contain numbers, not letters')
finally:
    print('Thanks')


# Thanks
try:
    int(123)
except ValueError:
    print('The string must contain numbers, not letters')
finally:
    print('Thanks')


# Something went wrong
# Thanks
try:
    a = int('123')
    a / 0           # ZeroDivisionError
except ValueError:
    print('The string must contain numbers, not letters')
except: 
    print('Something went wrong')
finally:
    print('Thanks')


with open('lorem-ipsum.txt') as file:
    try:
        file.readlines()
    except expression as identifier:    # as é para pegarmos na excepção e modificá-la no bloco except
        identifier


f = open('lorem-ipsum.txt')
try:
    #do something with file content
except expression as identifier:
    #handle exception
finally:
    f.close()








#**************************