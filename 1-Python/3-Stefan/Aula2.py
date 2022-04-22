# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 08:54:53 2020

@author: Ana Beatriz Varela
"""

#**************************

def multiplica_numero(numero, valor = 2):
    return numero * valor

print(multiplica_numero(2))         # 2 * 2 = 4
print(multiplica_numero(2, 3))      # 2 * 3 = 6

#**************************

a = [['a', 2], ['a', 0], ['b', 25], ['c', 0]]
a.sort()
print(a)                            # [['a', 0], ['a', 2], ['b', 25], ['c', 0]]

#**************************

def compare_items (item):
    return len(item[0])
    
a = [['a', 2], ['afgsjdg', 0], ['algkfdery', 25], ['ytukge', 0]]

a.sort(key=compare_items)
print(a)                            # ordena pelos valores, sendo que o primeiro não mexe

#**************************

def recursiva (a, b):
    return recursiva(a,b)
recursiva(1,2)                      # ERRO - Demasiadas recursões

#**************************

a = [1, 22, 33, 1, 16]
def lt_dezasseis (x):
    return x < 16

filtered_a = list(filter(lt_dezasseis, a))
print(filtered_a)

#**************************

lista_x = [1, 2, 3, 4]
a = [x + 2 for x in lista_x]
print(a)


lista_x = [1, 2, 3, 4]
result = []
for item in lista_x:
    result.append(item + 2)
print(result)

#**************************

a  = [[1, 2], [3, 4]]
flattened_a = [sub_item for item in a for sub_item in item]
print(flattened_a)

a  = [[1, 2], [3, 4]]
for item in a:
    for sub_item in item:
        print(sub_item)

a  = [[1, 2], [3, 4]]
result = []
for item in a:
    for sub_item in item:
        result.append(sub_item)
print(result)

a  = [[1, 2], [3, 4]]
result = []
for item in a:
    for sub_item in item:
        result.append(sub_item)
        print(result)

from functools import reduce
flattened_a = reduce(lambda x,y: x + y, a)
print(flattened_a)

#**************************

def funcao(x,y):        # Para aparecerem os parametros, basta escrever 3 ' (ou 3 ") e dar Enter
    '''
    

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''

#**************************

def potenciaP (a):
    return a**a
a = 2

print(potenciaP(a))


def potencia (a, b = a):
        return a**b
a = 2
b = 3

print(potencia(a, b))
print(potencia(a))


# Melhor solução
def potencia (a, b = None):
        return a ** a if b == None else a ** b
a = int(input('Valor 1: '))
b = int(input('Valor 2: '))

print(potencia(a, b))

#**************************

a = 4
def printFuncao():
    a = 17
    print("Dentro da função: ", a)

print












