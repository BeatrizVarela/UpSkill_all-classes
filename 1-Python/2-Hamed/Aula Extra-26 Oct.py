# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:14:42 2020

@author: Ana Beatriz Varela
"""

for i in range(3, 20, 4):
    print("first loop: ", i)
    
for i in list(range(3, 20, 4)):
    i += 2                          # acrescenta +2 a cada número
    print("second loop ", i)         
    
a, b = 2, 3

# Depois do if escreve-se sempre a variavel
for i in list(range(3, 20, 4)):
    if i > 7:                       # só imprime números acima de 7
        i += 2                      # acrescenta +2 a cada número
        print("third loop ", i)     # 13, 17, 21

for i in list(range(3, 20, 4)):
    if i in [7, 15, 10]:            # só imprime os números da sequência
        i += 2                      # acrescenta +2 a cada número
        print("4th loop ", i)       # 9, 17

for i in [3, 7, 11, 15, 19]:
    if i not in [7, 15, 10]:        # só imprime os números que não estão na sequência
        print("5th loop ", i)       # 3, 11, 19

for j in range(5, 10, 2):
    print(j, end = ' ')             # Imprimir na mesma linha!















